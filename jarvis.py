# import re
# from click import command
import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia

engine = pyttsx3.init("espeak")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# speak("Hello World")
def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)


    try:
        print("Wait for a few moments...")
        query = r.recognize_google(audio, language="en-us")
        print(f"You just said: {query}\n")
    except Exception as e:
        print(e)
        speak("Please tell me one more time")
        query = "none"

    return query

# query=commands().lower()
def myWish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        print("Good Morning Lone Wolf")
        speak("Good Morning Lone Wolf")
    elif hour>=12 and hour<=17:
        print("Good Afternoon Lone Wolf")
        speak("Good Afternoon Lone Wolf")
    elif hour>=17 and hour<=21:
        print("Good Evening Lone Wolf")
        speak("Good Evening Lone Wolf")
    else:
        print("Good Night Lone Wolf")
        speak("Good Night Lone Wolf")
if __name__ == "__main__":
    myWish()
    query=commands().lower()
    if 'time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M")
        print(strTime)
        speak(f"Sir, the time is {strTime}")
    elif 'open firefox' in query:
        speak("opening Firefox Application sir...")
        os.startfile(pathtofile)
    elif 'wikipedia' in query:
        speak("searching in wikipedia...")
        try:
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia, ")
            print(results)
            speak(results)
        except:
            speak("no results found")
            print("no results found")
    