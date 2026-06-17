# Easy TTS toolkit

![Static Badge](https://img.shields.io/badge/The-The)

Spoiler alert: this code is BAD
It's a bit rushed so there's not much consistency between how each file works. But all that matters is that it works. #Pragmatism #slop

This is my definitive easy use TTS toolkit! Written by [Miguel Arden](https://github.com/stealthmaster62)
You are welcome to do literally whatever you want with this code, credit is appreciated but not necessary.

### Billing and safety notice
This project includes examples for services that may charge based on usage. It does not include any API keys or account credentials.

- gTTS: free to use and requires no external API key.
- Azure: has a free tier, but it can charge if you exceed the quota or if your subscription is not on the free tier.
- Polly: AWS free tier is limited, and charges may apply after the allowance or after the first 12 months.
- ElevenLabs: includes a monthly free credit allotment, but usage beyond that will cost money in the
form of a paid subscription. Unless you enable pay as you go, you are at no risk of facing charges
without warning.

Use these services at your own risk. Monitor your account billing carefully and do not run large batches of text without understanding the cost.

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
gTTS is free. Azure and Polly may be free within their account limits, but those services can charge once you exceed the free quota or if your account is on a paid tier. ElevenLabs is the most likely to incur direct usage costs.

**Elevenlabs** - Very realistic sounding, recommended for reading long sentences especially if you'd like a lot of emotion throughout. You get a free 10,000 credits per month in the default plan. If you use more than the free credits, you will need to upgrade your subscription or pay for additional usage. Not sponsored!!!

**Microsoft Azure** - Robotic, similar to Polly voices but much more versatile. You have an option to write prefixes before text you want it to read which will change the way it sounds.
Example:
```python
speak("(shouting) I don't believe it!")
```
There's 11 voice styles you can use. The default voice style it uses if you don't use a prefix is "chat". You can view the list of styles in the Azure readme file.


**Polly** - Famously used in Twitch TTS a lot. It's likely you've heard these voices a lot. It's a simple voice, fun to listen to.


**gTTS** - Requires 0 setup and is completely free. Recommended for the most effortless experience adding this toolkit to your projects.

You can read more info about all of these in their respective readme files.

*hope you find this repo useful, I had fun making it! Apologies if it's crap*

## TODO
- Volume control

## Star History

<a href="https://www.star-history.com/?repos=stealthmaster62%2FEasy-TTS-Toolkit&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=stealthmaster62/Easy-TTS-Toolkit&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=stealthmaster62/Easy-TTS-Toolkit&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=stealthmaster62/Easy-TTS-Toolkit&type=date&legend=top-left" />
 </picture>
</a>
