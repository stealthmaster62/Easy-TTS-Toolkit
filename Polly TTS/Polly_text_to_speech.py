import os
import tempfile
import boto3
import sounddevice as sd
import soundfile as sf
import numpy as np

ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET = os.getenv("AWS_SECRET")
AWS_REGION = "eu-north-1"


client = boto3.client(
    'polly',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET,
    region_name=AWS_REGION
)

def speak(text):
    response = client.synthesize_speech(VoiceId='Brian',
                    Text=text,
                    OutputFormat='pcm',
                    Engine='standard')
    
    audio_data = response["AudioStream"].read()

    np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0