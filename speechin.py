import random
import pyttsx3
import speech_recognition as sr
import time
from subprocess import Popen
# import twiliogenericsmssender
from datetime import datetime
import calendar
import json



def generate_passphrase():
    words = ['ccokie', 'tea', 'coffee', 'traffic']
    choice =  random.choice(words)
    return choice




maindelay = 5  #delay for main loop

r = sr.Recognizer()


def getSpeech():
    text = "human"
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    

    text = text.lower()

    if "attack" in text:
        return "attack"

    if "run away" in text:
        return "escape"
    
    if "heal" in text:
        return "heal"

    if "defend" in text:
        return "defend"
    

    return "unknown"

def speak(sentence):
    eng = pyttsx3.init()
    eng.setProperty('rate', 130) 
    eng.say(sentence)
    eng.runAndWait()
    print(sentence)
    eng.stop() 

# name = input('what is your name?')
# n1 = len(name)

# name = getname()


