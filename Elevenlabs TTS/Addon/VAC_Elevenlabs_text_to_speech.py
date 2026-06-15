import os
import tempfile
from elevenlabs import play, stream
from elevenlabs.client import ElevenLabs
import sounddevice as sd
import soundfile as sf
from typing import IO
from io import BytesIO
import numpy as np

DEVICE_NAME = 'CABLE Input'

_device_index_cache = None

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def _get_device_index():
    global _device_index_cache

    if _device_index_cache is not None:
        return _device_index_cache

    for i, d in enumerate(sd.query_devices()):
        if DEVICE_NAME.lower() in d["name"].lower() and d["max_output_channels"] > 0:
            _device_index_cache = i
            return i

    raise ValueError(f"Audio device not found: {DEVICE_NAME}")


def speak(text: str):
    response = elevenlabs.text_to_speech.convert(
        voice_id="Hjzqw9NR0xFMYU9Us0DL",
        output_format="pcm_44000",
        text=text,
        model_id="eleven_flash_v2_5"
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        path = f.name

    with open(path, 'wb') as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    data = np.fromfile(path, dtype=np.int16).astype(np.float32) / 32768.0
    samplerate = 44000

    if data.ndim > 1:
        data = data.mean(axis=1)
    
    sd.play(data, samplerate, blocking=True, device=_get_device_index())

sd.stop()
    
