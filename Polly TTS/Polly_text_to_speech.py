import os
import tempfile
import boto3
import sounddevice as sd
import soundfile as sf
import numpy as np

polly_client = None
_voice_id = ""
    
polly_client = boto3.client(
    "polly",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("AWS_SECRET"),
    region_name=os.getenv("AWS_REGION", "eu-north-1")
)

_voice_id = "Brian"

def speak(text: str) -> None:
    if polly_client is None:
        raise RuntimeError("AWS Polly client is not initialised. Call init() first.")
    
    response = polly_client.synthesize_speech(
        Text=text,
        VoiceId=_voice_id,
        OutputFormat="pcm",
        Engine="standard"        
    )

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        path = f.name

    with open(path, 'wb') as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    data = np.fromfile(path, dtype=np.int16).astype(np.float32) / 32768.0
    samplerate = 44100

    if data.ndim > 1:
        data = data.mean(axis=1)
    
    sd.play(data, samplerate, blocking=True)

sd.stop()
    
