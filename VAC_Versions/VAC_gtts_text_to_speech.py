import tempfile
import gtts
import sounddevice as sd
import soundfile as sf

DEVICE_NAME = 'CABLE Input'

_device_index_cache = None


def _get_device_index():
    global _device_index_cache

    if _device_index_cache is not None:
        return _device_index_cache

    for i, d in enumerate(sd.query_devices()):
        if DEVICE_NAME.lower() in d["name"].lower() and d["max_output_channels"] > 0:
            _device_index_cache = i
            return i

    raise ValueError(f"Audio device not found: {DEVICE_NAME}")


def speak(text):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        temp_file_path = f.name

    tts = gtts.gTTS(text=text, lang='en')
    tts.save(temp_file_path)

    audio_samples, sample_rate = sf.read(temp_file_path, dtype="float32")

    if audio_samples.ndim > 1:
        audio_samples = audio_samples.mean(axis=1)

    sd.play(audio_samples,
        sample_rate,
        blocking=True,
        device=_get_device_index()
    )

    sd.stop()