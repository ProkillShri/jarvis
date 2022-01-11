import pyttsx3
import speech_recognition as sr
import wolframalpha
import requests

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


def WolfRam(query):
    api_key = "Q6J8G4-99GAKRVHW9"

    requester = wolframalpha.Client(api_key)

    requested = requester.query(query)

    try:

        Answer = next(requested.results).text

        return Answer

    except:
        speak("An error arrived")


kk = WolfRam('temperature in sagar')

print(kk)




def calculator(query):

    Term = str(query)

    Term = Term.replace("jarvis", "")
    Term = Term.replace("multiply", "*")
    Term = Term.replace("plus", "+")
    Term = Term.replace("minus", "-")
    Term = Term.replace("divided", "/")

    Final = str(Term)

    try:

        result = WolfRam(Final)
        speak(f"{result}")
        print(result)

    except:

        speak("No answerable data found")

calculator('8888888888888888888888 divided 8888888888888888888888 ')