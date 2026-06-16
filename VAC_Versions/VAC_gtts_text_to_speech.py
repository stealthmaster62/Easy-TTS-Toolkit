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

def speak(text_to_speak):

    sentences = [sentence.strip() for sentence in text_to_speak.split(". ") if sentence.strip()] 

    for sentence in sentences:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
            temp_file_path = temp_audio_file.name

        tts_engine = gtts.gTTS(text=sentence, lang='en')

        try:
            tts_engine.save(temp_file_path)
            
            raw_audio, sample_rate = sf.read(temp_file_path, dtype="float32")
            
            if raw_audio.ndim > 1:
                processed_audio = raw_audio.mean(axis=1)
            else:
                processed_audio = raw_audio

            sd.play(processed_audio,
                    sample_rate,
                    blocking=True,
                    device=_get_device_index())
        
        except (gtts.tts.gTTSError, sf.SoundFileError) as ahhellnah:
            print(f"gTTS generation error: {ahhellnah}")