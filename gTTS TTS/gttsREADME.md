Fortunately, GTTS literally requires 0 external setup

add gtts_text_to_speech.py (or the virtual audio cable version if needed) to any project

```python
from gtts_text_to_speech.py import speak

speak("hello")

#and of course, if you want to say a variable do:
var = 'test'
speak(f"this is a {var}")
#and it will say
```