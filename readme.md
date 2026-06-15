# Easy TTS toolkit

This is my definitive easy use TTS toolkit! Written by https://github.com/Miguel-Arden
You are welcome to do literally whatever you want with this code, credit is appreciated but not necessary.

It's very simple to use, literally as easy as a print statement once setup.

## Setup
1) This was written in Python 3.12.8. Install page here: https://www.python.org/downloads/release/python-3128/

2) Run "pip install -r requirements.txt" to install all the modules you'll need.

3) Take your pick at which voice you'd like to use in your project. I currently have 4 options of:
 - *Elevenlabs*
 - *Microsoft Azure*
 - *Amazon Polly*
 - *gTTS*

4) Whichever you choose. Make sure to go through the readme files there to figure out how to setup what you need to use it. The only 1 that requires 0 external setup is gTTS. If you're just looking to quickly implement TTS without worrying about how it sounds, I recommend that.

## Usage

Copy the file of your choice to anyone of your projects, all files have a test usage file that you can use before copying anything.

```python
from X_Text_to_speech import speak

speak("Test!")

#if you want the TTS to say a variable:
var = "test"

speak(f"hello this is a {var}")
```

## Voices
All the voices but Elevenlabs are practically free as the point of usage until it will cost you money is far beyond what most will ever use.

**Elevenlabs** - Very realistic sounding, recommended for reading long sentences especially if you'd like a lot of emotion throughout. You get a free 10000 credits per month. However you can upgrade your subscription to get more voices, and more credits. Not sponsored!!!

**Microsoft Azure** - Robotic, similar to Polly voices but much more versatile. You have an option to write prefixes before text you want it to read which will change the way it sounds.
Example:
```python
speak("(shouting) I don't believe it!")
```
There's 11 voice styles you can use. The default voice style it uses if you don't use a prefix is "chat". You can view the list of styles in the Azure readme file.


**Polly** - Famously used in Twitch TTS a lot. It's likely you've heard these voices a lot. It's a simple voice, fun to listen to.


**gTTS** - Requires 0 setup and is completely free. Recommended for the most effortless experience adding this toolkit to your projects.

You can read more info about all of these in their respective readme files.

*hope you find this file useful, I had fun making it!*