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


ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)


def speak(text: str):
    response = elevenlabs.text_to_speech.convert(
        voice_id="Hjzqw9NR0xFMYU9Us0DL",
        output_format="pcm_32000",
        text=text,
        model_id="eleven_flash_v2_5"
    )

    samplerate = 32000

    q = queue.Queue(maxsize=50)
    producer_done = threading.Event()

    def producer():
        for chunk in response:
            if chunk:
                q.put(chunk)
        producer_done.set()

    prod_thread = threading.Thread(target=producer, daemon=True)
    prod_thread.start()

    buf = bytearray()

    def callback(outdata, frames, time_info, status):
        nonlocal buf
        # outdata is float32 shape (frames, channels)
        needed_bytes = frames * 2  # int16 mono

        # Pull available chunks into buffer (non-blocking)
        try:
            while len(buf) < needed_bytes:
                item = q.get_nowait()
                buf.extend(item)
        except queue.Empty:
            pass

        if len(buf) >= needed_bytes:
            chunk = bytes(buf[:needed_bytes])
            del buf[:needed_bytes]
            arr = np.frombuffer(chunk, dtype=np.int16).astype(np.float32) / 32768.0
            outdata[:, 0] = arr
        else:
            # partial or empty - fill what we have then zero-fill rest
            avail_bytes = len(buf) - (len(buf) % 2)
            if avail_bytes > 0:
                chunk = bytes(buf[:avail_bytes])
                del buf[:avail_bytes]
                arr = np.frombuffer(chunk, dtype=np.int16).astype(np.float32) / 32768.0
                outdata.fill(0)
                outdata[:len(arr), 0] = arr
            else:
                outdata.fill(0)

        # stop when producer finished and no buffered data left
        if producer_done.is_set() and q.empty() and len(buf) == 0:
            raise sd.CallbackStop

    with sd.OutputStream(samplerate=samplerate, channels=1, dtype='float32', callback=callback):
        # block until stream stops
        while not (producer_done.is_set() and q.empty() and len(buf) == 0):
            time.sleep(0.02)


sd.stop()
