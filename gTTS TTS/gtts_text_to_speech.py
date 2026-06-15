import tempfile
import gtts
import sounddevice as sd
import soundfile as sf

def speak(text):

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        path = f.name

    tts = gtts.gTTS(text=text, lang='en')
    tts.save(path)

    data, samplerate = sf.read(path, dtype="float32")

    if data.ndim > 1:
        data = data.mean(axis=1)

    sd.play(data, samplerate, blocking=True)

    sd.stop()