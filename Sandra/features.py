# import main
import pywhatkit  # pip install pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow   # pip install pywikihow
from pywikihow import WikiHow, search_wikihow
import os
import speech_recognition as sr  # pip install speechRecognition
import webbrowser as web
import bs4
import pyttsx3      # pip install pyttsx3
from time import sleep
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(": Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f": Your Command : {query}\n")

    except:
        return ""
    return query.lower()


def GoogleSearch(term):
    query = term.replace("sandra", "")
    query = query.replace("what is", "")
    query = query.replace("how to", "")
    query = query.replace("what is", "")
    query = query.replace(" ", "")
    query = query.replace("what do you mean by", "")
    query = query.replace("google search", "")

    writeab = str(query)

    ggle = open('C:\\Project\\Desktop Assistant\\Sandra\\Data.txt', 'a')
    ggle.write(writeab)
    ggle.close()

    Query = str(term)
    pywhatkit.search(Query)

    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query, max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        speak(how_to_func[0].summary)
        # main.speak(how_to_func[0].summary)

    else:
        search = wikipedia.summary(Query, 2)
        speak(f": According To Your Search : {search}")
        #main.speak(f": According To Your Search : {search}")


def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    speak("This Is What I've Found For Your Search")
    pywhatkit.playonyt(term)
    speak("I Have Found Something ... This May Also Help You Sir")


def My_Location():
    op = "https://www.google.com/maps/place/Mumbai,+Maharashtra/@19.0821978,72.7411,57436m/data=!3m2!1e3!4b1!4m5!3m4!1s0x3be7c6306644edc1:0x5da4ed8f8d648c69!8m2!3d19.0759837!4d72.8776559"
    print("Tracking Your I P Address....")
    speak("Checking Your I P Address....")
    web.open(op)
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    state = geo_d['city']
    country = geo_d['country']
    speak(f"Sir , You Are Now In {state , country} .")
