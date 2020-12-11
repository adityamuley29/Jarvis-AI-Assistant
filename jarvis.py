import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
from security import email_id,password




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def start():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Aditya!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Aditya! ")
    else:
        speak("Good Evening Aditya!")
    
    speak("Hello , I am Jarvis . How can i help you?")

def takeCommand():
    # It takes microphone input from the user and returns string as a output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said :- {query}\n ")
    except Exception as e:
        # print(e)
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to , content):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(email_id,password)
    server.sendmail(email_id,to,content)
    server.close()


if __name__ == "__main__":
    start()
    while True:
        query = takeCommand().lower()

        # Logic for execuiting task based on query
        if 'wikipedia' in query:
            speak('Spearching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\Entertainment\music'
            songs = os.listdir(music_dir)
            random_song = random.randint(0,len(songs)-1)
            print(f"Now Playing :- {songs[random_song]}")
            os.startfile(os.path.join(music_dir,songs[int(random_song)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime} ")
        elif 'open vs code' in query:
            vsCode_path = "C:\\Users\\real\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening vs code")
            os.startfile(vsCode_path)
        elif 'open pycharm' in query:
            pycharm_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            speak("opening pycharm")
            os.startfile(pycharm_path)

        elif 'send email to aditya' in query:
            try:
                speak("What you want to say?")
                content = takeCommand()
                to = "adityamuley48@gmail.com"
                sendEmail(to , content)
                speak("Email has been send successfuly!")
            except Exception as e:
                print(e)
                speak("I'm really sorry . I'm not abe to send the email.")


