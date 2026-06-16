## Microsoft Azure

In this file I'll run through:
- How to properly setup Microsoft azure
- And how to use this file.

## Setting up your Azure account
1) go to https://portal.azure.com and create an account. 

2) find "create a resource" and search for Speech. Select the one made by Microsoft.

3) create it and pick your region. I picked "eastus" and have no issues despite not being in that region. Then select free tier

4) once the resource has deployed find "Keys and endpoint", copy your key and put that into your environment variables listed as "AZURE_SPEECH_KEY"

I'm pretty positive that the free tier gives you 500k characters a month permanently, so it shouldn't charge you anything.

## Usage

There's 2 files here, the main one is "Azure_Text_to_speech.py", the other one is an addon for those of you who need to make
use of virtual audio cables. If you're using this file and want your audio to be heard on OBS or something, that's when you'll need
to use 
If you are using the VAC version make sure to read the README file for that too. The Virtual audio cable versions are there for a personal
inconvenience I frequently have in getting my TTS voices to be heard on OBS in their own track. If you don't need them just delete them.

make sure to run run "pip install -r requirements.txt" in the terminal to install all the modules.

once you've installed the requirements, copy the azure file into a project of your choice.
then you can use
```python
speak("X")
```

You can also add voice styles before your text to change the way the voice speaks.

currently you can use:
- "cheerful"
- "chat"
- "sad"
- "angry"
- "excited"
- "friendly"
- "hopeful"
- "shouting"
- "terrified"
- "unfriendly"
- "whispering"

It defaults to use the Chat style if you don't use a prefix.

