import os
from elevenlabs import play, stream
from elevenlabs.client import ElevenLabs
import sounddevice as sd
import soundfile as sf
import numpy as np


ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def speak(text: str):
    response = elevenlabs.text_to_speech.convert(
        voice_id="Hjzqw9NR0xFMYU9Us0DL",
        output_format="mp3_44100_128",
        text=text,
        model_id="eleven_flash_v2_5"
    )
    play(response)
