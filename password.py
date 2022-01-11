import speech_recognition as sr
import pyttsx3
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("I cannot understand please say that again")
        return "None"
    return query


def Pass(pass_inp):
    password = "Prokiller gamer"

    passss = str(password)

    if passss == str(pass_inp):
        speak("Access Granted")
        print("Access Granted")
        os.startfile(r'C:\Users\Priya\PycharmProjects\Assistant\jarvis.py')



    else:
        speak("Access Not GRANTED")
        print("Access Not Granted")


if __name__ == "__main__":
    print("This File Is Password Protected ")
    speak("This File Is Password Protected ")
    print("Kindly Provide The Password To Accesss")
    speak("Kindly Provide The Password To Accesss")
    passssssss = input(":Enter the password:")



    Pass(passssssss)