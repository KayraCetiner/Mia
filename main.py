import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from time import sleep
import pyautogui
import webbrowser
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        voice = r.listen(source)
    command = None
    try:
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mia' in command:
                command = command.replace('mia', '')
    except:
        pass

    return command

def run_mia():
    command = take_command()
    if command is None:
        print("Can't understand")
    elif 'play' in command:
        song = command.replace('play', '')
        print(song)
        talk('playing')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is ' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
    elif "spotify" in command:
        print("Opening Spotify")
        webbrowser.open(url="https://open.spotify.com/playlist/1jdLFxxCUdaW0cSGZEwacr?si=b147e7230d1e4835")
        sleep(10)
        try:
            x, y = 965, 973
            pyautogui.click(x, y)

        except:
            print("Not Successful")
    elif "beyond" in command:
        os.system("C:\Program Files (x86)\Steam\steamapps\common\BEYOND Two Souls\BeyondTwoSouls_Steam.exe")
    else:
        print("Please say that again, maybe I can't do that")


while True:
    run_mia()

