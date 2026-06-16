import os
import tempfile
from elevenlabs import play, stream
from elevenlabs.client import ElevenLabs
import sounddevice as sd
import soundfile as sf
from typing import IO
from io import BytesIO
import numpy as np
import threading
import queue
import time

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
        output_format="pcm_32000",
        text=text,
        model_id="eleven_flash_v2_5"
    )

    samplerate = 32000

    audio_queue = queue.Queue(maxsize=50)
    producer_done = threading.Event()

    def producer():
        for chunk in response:
            if chunk:
                audio_queue.put(chunk)
        producer_done.set()

    prod_thread = threading.Thread(target=producer, daemon=True)
    prod_thread.start()

    buf = bytearray()

    def callback(outdata, frames, time_info, status):
        nonlocal buf
        needed_bytes = frames * 2  # int16 mono

        try:
            while len(buf) < needed_bytes:
                item = audio_queue.get_nowait()
                buf.extend(item)
        except queue.Empty:
            pass

        if len(buf) >= needed_bytes:
            chunk = bytes(buf[:needed_bytes])
            del buf[:needed_bytes]
            arr = np.frombuffer(chunk, dtype=np.int16).astype(np.float32) / 32768.0
            outdata[:, 0] = arr
        else:
            avail_bytes = len(buf) - (len(buf) % 2)
            if avail_bytes > 0:
                chunk = bytes(buf[:avail_bytes])
                del buf[:avail_bytes]
                arr = np.frombuffer(chunk, dtype=np.int16).astype(np.float32) / 32768.0
                outdata.fill(0)
                outdata[:len(arr), 0] = arr
            else:
                outdata.fill(0)

        if producer_done.is_set() and audio_queue.empty() and len(buf) == 0:
            raise sd.CallbackStop

    device_index = _get_device_index()
    with sd.OutputStream(samplerate=samplerate, channels=1, dtype='float32', callback=callback, device=device_index):
        while not (producer_done.is_set() and audio_queue.empty() and len(buf) == 0):
            time.sleep(0.02)
    
