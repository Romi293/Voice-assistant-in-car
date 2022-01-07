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
    print("Exit")
    talk("Goodbye")
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


def time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    talk('the time is' + time)
    print(time)


def playYouTube(command):
    song = command.replace('play', '')
    talk('playing' + song + '. I wont disturb you, enjoy!')
    # open YouTube to play
    pywhatkit.playonyt(song)
    exit(0)


def googleSearch(command):
    google = command.replace('search for', '')
    talk('search' + google)
    pywhatkit.info(google)


def wikiSearch(command):
    wisdom = command.replace('Im searching in wikipedia', '')
    info = wikipedia.summary(wisdom, 1)
    print(info)
    talk(info)


def navigate(command):
    location = command.replace('navigate to', '')
    talk('navigate to' + location)
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

        talk("The message " + msg + " was sent to " + receiver + " successfully")
        print("The message " + msg + " was sent to " + receiver + " successfully")
    first = False
    return first

    # pywhatkit.sendwhatmsg("=+972528620066", "Hello Romi", 20, 31)


def take_command():
    try:
        # set the voice commend trow mic
        with sr.Microphone() as source:
            # verified that the assistant listen
            # save the sentence
            voice = listener.listen(source)
            # send the sentence to google
            command = listener.recognize_google(voice)
            command = command.lower()
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
    global first
    print(str(first))
    if first:
        talk("What can I do for you?")
        command = take_command()
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
        command = take_command()
        if 'yes' in command:
            first = True
            run_REA()
        elif 'no' in command:
            exit_REA()
    first = False


while True:
    greeting()
    run_REA()
