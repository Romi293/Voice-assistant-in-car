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

# true if it's the first entrance to the system each time
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
engine.setProperty('rate', 130)
engine.setProperty('voice', voices[2].id)


def talk(text):
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


def time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    talk('the time is' + time)
    print(time)


def playYouTube(command):
    song = command.replace('play', '')
    talk('playing' + song + '. I wont disturb you, enjoy!')
    print("Playing " + song)
    # open YouTube to play
    pywhatkit.playonyt(song)
    exit(0)


def googleSearch(command):
    google = command.replace('search for', '')
    talk('searching for ' + google)
    print("Searching for " + google)
    pywhatkit.info(google)


def wikiSearch(command):
    wisdom = command.replace('Im searching in wikipedia', '')
    info = wikipedia.summary(wisdom, 1)
    print(info)
    talk(info)


def navigate(command):
    location = command.replace('navigate to', '')
    talk('navigate to' + location)
    print("Navigate to " + location)
    webbrowser.open("https://www.google.com/maps/place/" + location)


def sendWhatsapp(command):
    with sr.Microphone() as source:
        talk("To whom do you want to send?")
        receiver = command.replace('send to', '')
        voice = listener.listen(source)
        # send the sentence to google
        receiver = listener.recognize_google(voice)

        talk("What do you want to send?")
        voice = listener.listen(source)
        # send the sentence to google
        msg = listener.recognize_google(voice)

        hour = datetime.datetime.now().hour
        minutes = datetime.datetime.now().minute

    pywhatkit.sendwhatmsg("=+972528620066", msg, hour, minutes + 1)
    talk("The message " + msg + " was sent to " + receiver + " successfully")
    print("The message " + msg + " was sent to " + receiver + " successfully")

    first = False
    return first


def listening():
    with sr.Microphone() as source:
        # save the sentence
        voice = listener.listen(source)
        # send the sentence to google
        command = listener.recognize_google(voice)
        print(command)
    return command


def run_REA():
    greeting()
    global first
    if first:
        talk("What can I do for you?")
        command = listening()
        if 'play' in command:
            playYouTube(command)
        elif 'send' in command:
            sendWhatsapp(command)
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
        first = False
    else:
        talk("Do you need something else?")
        command = listening()
        print(command)
        if 'yes' in command:
            first = True
        elif 'no' in command:
            exit_REA()
            first = False


while True:
    run_REA()
