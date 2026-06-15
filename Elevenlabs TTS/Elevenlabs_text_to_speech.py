import os
from typing import IO
from io import BytesIO
from elevenlabs.client import ElevenLabs
import sounddevice as sd
import soundfile as sf

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def speak(text: str) -> IO[bytes]:
    response = elevenlabs.text_to_speech.stream(
        voice_id="Hjzqw9NR0xFMYU9Us0DL",
        output_format="pcm_32000",
        text=text,
        model_id="eleven_flash_v2_5"
    )

    audio_stream = BytesIO()

    for chunk in response:
        if chunk:
            audio_stream.write(chunk)

    audio_stream.seek(0)

    return audio_stream
