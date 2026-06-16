import os
import random
import tempfile
import azure.cognitiveservices.speech as speechsdk
import sounddevice as sd
import soundfile as sf

SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY")
SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION", "eastus")

if not SPEECH_KEY:
    raise ValueError("Missing AZURE_SPEECH_KEY")

#find more voices on the azure website
VOICE = "en-US-DavisNeural"
DEVICE_NAME = "CABLE Input"  # VB-Cable output target

STYLES = [
    "cheerful",
    "chat",
    "sad",
    "angry",
    "excited",
    "friendly",
    "hopeful",
    "shouting",
    "terrified",
    "unfriendly",
    "whispering",
]

STYLE_PREFIXES = {
    "(angry)": "angry",
    "(chat)": "chat",
    "(cheerful)": "cheerful",
    "(excited)": "excited",
    "(friendly)": "friendly",
    "(hopeful)": "hopeful",
    "(sad)": "sad",
    "(shouting)": "shouting",
    "(shout)": "shouting",
    "(terrified)": "terrified",
    "(unfriendly)": "unfriendly",
    "(whispering)": "whispering",
    "(whisper)": "whispering",
    "(random)": "random",
}

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


def speak(text: str, style: str = None):

    detected_style = None


    for prefix, mapped_style in STYLE_PREFIXES.items():
        if text.lower().startswith(prefix):
            detected_style = mapped_style
            text = text[len(prefix):].strip()
            break


    if detected_style == "random":
        style = random.choice(STYLES)
    elif detected_style:
        style = detected_style
    elif style is None:
        style = random.choice(STYLES)


    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
        temp_file_path = temp_audio_file.name

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=speechsdk.audio.AudioOutputConfig(filename=temp_file_path)
    )

    ssml = f"""
<speak version='1.0'
 xmlns='http://www.w3.org/2001/10/synthesis'
 xmlns:mstts='http://www.w3.org/2001/mstts'
 xml:lang='en-US'>

    <voice name='{VOICE}'>
        <mstts:express-as style='{style}'>
            {text}
        </mstts:express-as>
    </voice>

</speak>
"""

    result = synthesizer.speak_ssml_async(ssml).get()

    if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
        raise RuntimeError(f"TTS failed: {result.reason}")

    audio_samples, sample_rate = sf.read(temp_file_path, dtype="float32")

    if audio_samples.ndim > 1:
        audio_samples = audio_samples.mean(axis=1)

    sd.play(
        audio_samples,
        sample_rate,
        device=_get_device_index(),
        blocking=True
    )

    sd.stop()