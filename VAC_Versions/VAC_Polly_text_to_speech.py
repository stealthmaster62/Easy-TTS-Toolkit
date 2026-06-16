import os
import boto3
import sounddevice as sd
import numpy as np

DEVICE_NAME = 'CABLE Input'

_device_index_cache = None

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET = os.getenv("AWS_SECRET")
AWS_REGION = "eu-north-1"

client = boto3.client(
    'polly',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET,
    region_name=AWS_REGION
)


def _get_device_index():
    global _device_index_cache

    if _device_index_cache is not None:
        return _device_index_cache
    
    for device_index, device_info in enumerate(sd.query_devices()):
        if DEVICE_NAME.lower() in device_info["name"].lower() and device_info["max_output_channels"] > 0:
            _device_index_cache = device_index
            return device_index
        
        raise ValueError(f"audio device not found: {DEVICE_NAME}")
    

def speak(text):
    response = client.synthesize_speech(VoiceId='Brian',
                    Text=text,
                    OutputFormat='pcm',
                    Engine='standard',
                    SampleRate='16000')
    
    audio_data = response["AudioStream"].read()

    samples = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0

    sd.play(
        samples,
        samplerate=16000,
        blocking=True,
        device=_get_device_index
    )
