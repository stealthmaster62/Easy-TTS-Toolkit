## Google TTS
Fortunately, GTTS literally requires 0 external setup, but it does sound the worst.

### Cost and billing
gTTS uses Google's text-to-speech backend through the free translation API and does not require an API key. It is free for normal use.

once you've installed the requirements, copy the gtts file into a project of your choice. Then do:

```python
from gtts_text_to_speech.py import speak

speak("awfoijrfopjrtojgo")
```