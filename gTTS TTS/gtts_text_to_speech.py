import gtts
import tempfile
import soundfile as sf
import sounddevice as sd

def speak(text_to_speak):

    sentences = [sentence.strip() for sentence in text_to_speak.split(". ") if sentence.strip()] 

    for sentence in sentences:
        temp_file_path = None
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
                temp_file_path = temp_audio_file.name

            tts_engine = gtts.gTTS(text=sentence, lang='en')
            tts_engine.save(temp_file_path)

            raw_audio, sample_rate = sf.read(temp_file_path, dtype="float32")

            if raw_audio.ndim > 1:
                processed_audio = raw_audio.mean(axis=1)
            else:
                processed_audio = raw_audio

            sd.play(processed_audio, sample_rate, blocking=True)

        except (gtts.tts.gTTSError, sf.SoundFileError) as ahhellnah:
            print(f"gTTS generation error: {ahhellnah}")
        finally:
            if temp_file_path and os.path.exists(temp_file_path):
                os.remove(temp_file_path)