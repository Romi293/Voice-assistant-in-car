# allow using voice commend
import sys

import speech_recognition as sr
# allow to the assistant to return an answer
import pyttsx3

# allow accuses to other apps
import pywhatkit

# allow access to time
import datetime
import time

# allow access to web wisdom
import wikipedia

import webbrowser

# allows saving voice commend
listener = sr.Recognizer()

# allow to the assistant to return an answer
engine = pyttsx3.init()
# get a voice
voices = engine.getProperty('voices')
# set it to the program
engine.setProperty('rate', 130)
engine.setProperty('voice', voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def exit_REA():
    print("Exit")
    talk("Have a nice day")
    sys.exit(0)


def greeting():
    currentTime = datetime.datetime.now()
    currentTime.hour
    if currentTime.hour < 12:
        talk('Good morning')
    if 12 < currentTime.hour < 18:
        talk('Good afternoon')
    if currentTime.hour > 18:
        talk('Good evening')


def time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    talk('the time is' + time)
    print(time)


def playYouTube(command):
    song = command.replace('play', '')
    talk('playing' + song)
    # open YouTube to play
    pywhatkit.playonyt(song)


def googleSearch(command):
    google = command.replace('search for', '')
    talk('search' + google)
    pywhatkit.search(google)


def wikiSearch(command):
    wisdom = command.replace('Im searching in wikipedia', '')
    info = wikipedia.summary(wisdom, 1)
    print(info)
    talk(info)


def navigate(command):
    location = command.replace('navigate to', '')
    talk('navigate to' + location)
    webbrowser.open("https://www.google.com/maps/place/" + location)


def take_command(x):
    try:
        # set the voice commend trow mic
        with sr.Microphone() as source:
            # verified that the assistant listen
            if x > 1:
                talk("What can I do for you?")
                # save the sentence
                voice = listener.listen(source)
                # send the sentence to google
                command = listener.recognize_google(voice)
                command = command.lower()
            else:
                talk("Do you need something else?")
                # save the sentence
                voice = listener.listen(source)
                # send the sentence to google
                command = listener.recognize_google(voice)
                command = command.lower()
            x += 1
            '''
            if 'rea' in command:
                # remove a word from speech
                command = command.replace('alexa', '')
                print("yeah!")
            # verified that the voice is equal to the Google recognizer
            else:
                print(command)
            '''
    except:
        pass
    return command


def run_REA():
    flag = 1
    command = take_command(flag)
    if 'play' in command:
        playYouTube(command)
    elif 'what is the time' in command:
        time()
    elif 'wikipedia' in command:
        wikiSearch(command)
    elif 'google' in command:
        googleSearch(command)
    elif 'navigate' in command:
        navigate(command)
    elif 'goodbye' or 'bye bye' or 'exit' or 'nothing' or 'no' in command:
        exit_REA()
    else:
        talk("Please say it again")
    return flag


while True:
    greeting()
    run_REA()
