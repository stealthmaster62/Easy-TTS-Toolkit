import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Elevenlabs_text_to_speech import speak
#from VAC_Versions.VAC_Elevenlabs_text_to_speech import speak

speak("Testing Elevenlabs TTS! Boy I sure do feel like starring the repo I downloaded this from!")


#if you want the TTS to say a variable.
var = "test"

speak(f"hello this is a {var}")
#if testing with the VAC version remove the hashtag in front of line 2 and delete line 1
