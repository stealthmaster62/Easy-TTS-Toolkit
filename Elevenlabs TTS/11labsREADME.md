## Elevenlabs

Elevenlabs has some realistic sounding voices that are incredibly fun to use.

This is the highest quality of the 4 you can choose from, but the most expensive.

## Setup

1) go to https://elevenlabs.com and create an account

2) then go to https://elevenlabs.io/app/developers/api-keys and create an API key. Copy it and add it to your environment variables under "ELEVENLABS_API_KEY"

3) Run "pip install -r requirements.txt" to install all modules.

4) once you've installed the requirements, copy the file into a project of your choice.
then do:
```python
from Elevenlabs_text_to_speech.py import speak

speak("I am bald")
```
