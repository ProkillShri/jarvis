import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import pywhatkit
from win10toast import ToastNotifier
import psutil
import speedtest
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening!")

    speak("I am jarvis  your servant . Please tell me how can I help you")


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



toast = ToastNotifier()
toast.show_toast("Jarvis", "The Jarvis is now activated", duration=3)

if __name__ == "__main__":
    wishMe()
    while True:
        query = TakeCommand().lower()
        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open_new_tab("youtube.com")

        elif 'open google' in query:
            speak("opening google")
            webbrowser.open_new_tab("google.com")

        elif 'open stack overflow' in query:
            speak("opening stackoverflow")
            webbrowser.open_new_tab("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'joke' in query:
            speak(pyjokes.get_jokes())
            print("pyjokes.get_jokes()")

        elif 'who are you' in query:
            speak("Your servant")

        elif 'facebook' in query:
            speak("opening facebook")
            webbrowser.open_new_tab("facebook.com")

        elif 'instagram' in query:
            speak("opening instagram")
            webbrowser.open_new_tab("instagram.com")

        elif 'new tab of google' in query:
            webbrowser.open_new_tab("google.com")

        elif 'open pipe' in query:
            webbrowser.open_new_tab("pypi.org")

        elif 'you are over power' in query:
            speak("Thank you sir")

        elif 'how are you' in query:
            speak("I am very good sir")

        elif 'take a break' in query:
            speak("ok sir")
            break

        elif 'track my amazon parcel' in query:
            speak("tracking the parcel")
            webbrowser.open_new_tab("https://www.amazon.in/gp/css/order-history?ref_=nav_orders_first")

        elif 'google search ' in query:
            import wikipedia as googleScrap

            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            query = query.replace("google", "")
            speak("this is what I found for your search")

            try:
                pywhatkit.search(query)
                result = googleScrap.summary(query, 3)
                speak(result)
                print(result)

            except:
                speak("no speakable data found")

        elif 'today news' in query:
            webbrowser.open("https://www.indiatoday.in/news.html")

        elif 'date' in query:
            date = int(datetime.datetime.now().day)
            speak(f"Sir today is {date} ")
            print(date)

        elif 'month' in query:
            month = int(datetime.datetime.now().month)
            speak(f"Sir this is the {month} month of the year")
            print(month)

        elif 'year' in query:
            year = int(datetime.datetime.now().year)
            speak(f"Sir the year is {year}")
            print(year)

        elif 'very good' in query:
            speak("Thank you sir , if you want any later service later please call me with wake up command")

        elif 'battery percentage' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"The battery percentage is {percentage} percent battery")
            print(percentage)
            if percentage>= 48:
                no_battery = ToastNotifier()
                no_battery.show_toast("Jarvis","Charge your device", duration=3)


        elif 'internet speed' in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir we have {dl} bits per second downloading speed and {up} bits per second uploading speed")
            print(dl),
            print(up)

        elif 'temperature' in query:
            search = "temperature in Sagar "
            url = f"https://www.google.com/search?q={query}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {query} is {temp}")
            print(temp)

        elif 'activate how to do mode' in query:
            speak("How to do mode is activated tell me what you want to do")
            how = TakeCommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)