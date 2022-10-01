import os
import pyttsx3
import speech_recognition as sr
import geocoder                          # pip install geocoder
import webbrowser as web

from datetime import datetime
from geopy.distance import great_circle  # pip install geopy
from geopy.geocoders import Nominatim
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from pyautogui import click              # pip install Keyboard
from os import startfile
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")


def takeCommand():
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


def GoogleMaps(Place):
    Url_Place = "https://www.google.com/maps/place/" + str(Place)
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(Place, addressdetails=True)
    target_latlon = location.latitude, location.longitude
    web.open(url=Url_Place)
    location = location.raw['address']
    target = {'city': location.get('city', ''),
              'state': location.get('state', ''),
              'country': location.get('country', '')}
    current_loca = geocoder.ip('me')
    current_latlon = current_loca.latlng
    distance = str(great_circle(current_latlon, target_latlon))
    distance = str(distance.split(' ', 1)[0])
    distance = round(float(distance), 2)
    speak(target)
    speak(f"Sir , {Place} iS {distance} Kilometre Away From Your Location . ")


def Notepad():
    speak("Tell Me The Query .")
    speak("I Am Ready To Write .")
    writes = takeCommand()
    time = datetime.now().strftime("%H:%M")
    filename = str(time).replace(":", "-") + "-note.txt"
    with open(filename, "w") as file:
        file.write(writes)
    path_1 = "C:\\Project\\Sandra\\" + str(filename)
    path_2 = "C:\\Project\\Sandra\\Database\\Notepad\\Output\\" + str(filename)
    os.rename(path_1, path_2)
    os.startfile(path_2)
