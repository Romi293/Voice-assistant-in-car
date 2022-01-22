# allow using voice commend
import os
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

import winsound

# true if it's the first entrance to the system each time
import GUI

global first
first = True

global once_greet
once_greet = True

# allows saving voice commend
listener = sr.Recognizer()

# allow to the assistant to return an answer
engine = pyttsx3.init()
# get a voice
voices = engine.getProperty('voices')
# set it to the program
engine.setProperty('rate', 180)
engine.setProperty('voice', voices[1].id)


def listening():
    frequency = 300  # Set Frequency To 2500 Hertz
    duration = 200  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)

    with sr.Microphone() as source:
        # save the sentence
        voice = listener.listen(source)
        # send the sentence to google
        command = listener.recognize_google(voice)
        command = command.lower()
        print("Driver: " + command.capitalize())
        return command


def talk(text):
    print("REA: " + text.capitalize())
    engine.say(text)
    engine.runAndWait()


def exit_REA():
    talk("Goodbye")
    print("Exit")
    sys.exit(0)


def greeting():
    global once_greet
    if once_greet:
        currentTime = datetime.datetime.now()
        if currentTime.hour < 12:
            talk('Good morning')
        if 12 < currentTime.hour < 18:
            talk('Good afternoon')
        if currentTime.hour > 18:
            talk('Good evening')
    else:
        pass
    once_greet = False


def clocktime():
    clock = datetime.datetime.now().strftime('%H:%M:%S')
    talk('the time is ' + clock)
    print(clock)


def playYouTube(command):
    song = command.replace('play', '')
    talk('playing' + song + '. I won' + "'" + 't disturb you, enjoy!'.capitalize())
    # open YouTube to play
    pywhatkit.playonyt(song)
    exit(0)


def googleSearch(command):
    google = command.replace('search for', '')
    google = google.replace('on google', '')
    talk('searching' + google + 'on Google')
    pywhatkit.search(google)


def wikiSearch(command):
    wisdom = command.replace('Im searching in wikipedia', '')
    info = wikipedia.summary(wisdom, 1)
    talk(info)


def navigate(command):
    location = command.replace('navigate to', '')
    talk('navigating to' + location)
    webbrowser.open("https://www.google.com/maps/place/" + location)


def sendWhatsapp(name, msg):
    hour = datetime.datetime.now().hour
    minutes = datetime.datetime.now().minute
    if 'Alex' in name:
        pywhatkit.sendwhatmsg("", msg, hour, minutes + 1)   # Enter phone number
    elif 'John' in name:
        pywhatkit.sendwhatmsg("", msg, hour, minutes + 1)   # Enter phone number
    else:
        pywhatkit.sendwhatmsg("", msg, hour, minutes + 1)


def run_REA():
    greeting()
    global first
    if first:
        talk("What can I do for you?")
        command = listening()
        if 'play' in command:
            playYouTube(command)
        elif 'send' in command:
            talk("To whom do you want to send?")
            command = listening()
            name = command
            talk("What do you want to send?")
            msg = listening()
            talk("The message " + msg + " will be sent to " + name + " in a couple of seconds")
            sendWhatsapp(msg, name)
        elif 'what is the time' in command:
            clocktime()
        elif 'know' in command:
            wikiSearch(command)
        elif 'google' in command:
            googleSearch(command)
        elif 'navigate' in command:
            navigate(command)
        elif 'exit' in command:
            exit_REA()
        else:
            talk("Please say it again")
            run_REA()
        first = False
    else:
        talk("Do you need something else?")
        command = listening()
        if 'yes' in command:
            first = True
        elif 'no' in command:
            exit_REA()
            first = False


if __name__ == "__main__":
    GUI.openWindow()
