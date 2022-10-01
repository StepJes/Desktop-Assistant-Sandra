# import automations
import ctypes
import datetime
# import features
import feedparser
import json
import os
import operator
from urllib import request
import pyjokes   # pip install pyjokes
import pyttsx3  # pip install pyttsx3
import random
import smtplib
import speech_recognition as sr  # pip install speechRecognition
import shutil
import sys
import subprocess
import time
from urllib.request import urlopen
import webbrowser
import wikipedia  # pip install wikipedia
import win32com.client as wincl
import winshell

from bs4 import BeautifulSoup
from doctest import master
from email.mime import audio
from features import GoogleSearch
from features import YouTubeSearch
from matplotlib.pyplot import text
# from notifypy import Notify          # pip install notifypy
from playsound import playsound  # pip install playsound
from types import coroutine
# from unittest import result
from win10toast import ToastNotifier  # pip install win10toast


# before installing the packages, check if the pyhton was installed in all path (Global) and added to path
# pip install pipwin
# py -m pip install PyAudio

# pip install flask
# because if incomplete request

print("Initializing Sandra Your Desktop Assistant...")

MASTER = "Stephen"

engine = pyttsx3.init('sapi5')  # sapi5 is a variable to activate it
voices = engine.getProperty('voices')
# 0 for male voice and 1 for female voice
engine.setProperty('voice', voices[1].id)

# Speak function will read out the string which is passed to it


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function will wish according to current time


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)

    elif hour >= 12 and hour < 16:
        speak("Good Afternoon" + MASTER)

    else:
        speak("Good Evening" + MASTER)

    speak("I am Sandra. How may I help you?")

# This function will take command from Microphone


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Could You Say that again")
        query = None
    return query


def sendEmail(to, content):
    # Using SMPT Server to write emails through gmail account
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # For security and private reasons don't use personal and confidential EmailID
    # before closing the server by server.close() , do the following steps
    # 1. 'search allow unsafe apps gmail' in browser/google
    # 2. Open 1st link which displays 'Less secure apps & your Google Account'
    # 3. Under 'If "Less secure app access' is on for your account' click on 'Less secure app access'
    # 4. Switch to the dummy account in use
    # 5. Toogle ON 'Allow less secure apps'     |    like....     Allow less secure apps: ON
    # Note: Account should not be  2-Step Verification enabled. It will pop up 'This setting is not available for accounts with 2-Step Verification enabled. Such accounts require an application-specific password for less secure apps access'

    # ('youremailid@gmail.com', 'emailID_password')
    server.login('itprojectpurpose@gmail.com', 'itpr0j3ctpurp0s3')
    #server.sendmail("*email*@gmail.com", to, content)
    server.close()
    # more detail in SMTP Documentation


# Main Program starts here
def main():

    # speak("Initializing Derrick...")
    wishMe()
    query = takeCommand()

    # Logic for executing tasks based on query

    if 'wikipedia' in query.lower():
        speak('Searching in wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        print(results)
        speak(results)

    elif 'browse' in query:
        print(query)
        print("Collecting Data...")
        speak("Just a Second ... Fetching and Collecting Data on it")
        query = query.replace("browse", "")
        query = query.replace("play", "")
        print("Here You go...")
        speak("look what i found")
        webbrowser.open(query)

    elif 'google me' in query.lower():
        speak('Searching in google...')
        GoogleSearch(query)

    # Perfoming tasks via Chrome

    elif 'open youtube' in query.lower():
        # webbrowser.open("youtube.com") # This will directly open bydefault in Microsoft Edge
        url = "youtube.com"
        chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
        # Here double-inverted Comma inside Single-inverted comma is necessary for accepting the Location of chrome
        speak("initializing Chrome... Opening youtube")
        print("Opening YouTube...")
        webbrowser.get(chrome_path).open(url)
        # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        # webbrowser.get(chrome_path).open(url)

    elif 'YouTube for' in query:
        Query = query.replace("sandra", "")
        query = Query.replace("youtube for", "")
        from features import YouTubeSearch
        YouTubeSearch(query)

    elif 'open google' in query.lower():
        url = "google.com"
        chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
        speak("initializing Chrome... Opening google")
        print("Opening Google...")
        webbrowser.get(chrome_path).open(url)

    elif 'open stack overflow' in query.lower():
        url = "stackoverflow.com"
        chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
        speak("initializing Chrome... Opening stack overflow")
        print("Opening Stackoverflow...")
        webbrowser.get(chrome_path).open(url)

    elif 'open reddit' in query.lower():
        url = "reddit.com"
        chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
        speak("initializing Chrome... Opening reddit")
        print("Opening Reddit...")
        webbrowser.get(chrome_path).open(url)

    elif 'facebook' in query.lower():
        url = "facebook.com"
        chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
        speak("Contacting mark zuckerberg ... Opening facebook")
        print("Opening Facebook...")
        webbrowser.get(chrome_path).open(url)

    elif 'instagram' in query.lower():
        url = "instagram.com"
        chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
        speak("initializing Chrome... Opening instagram")
        print("Opening Instagram...")
        webbrowser.get(chrome_path).open(url)

    elif 'open bible' in query.lower():
        url = "https://www.kingjamesbibleonline.org/"
        chrome_path = '"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
        speak("initializing Chrome... Opening bible, the Word of GOD")
        print("Opening BIBLE...")
        webbrowser.get(chrome_path).open(url)

    # Task of Playing Music in system
    elif 'play music' in query.lower() or "play song" in query.lower():
        speak("Here you go with your music")
        print("Playing Music...")
        songs_dir = "C:\\Project\\Sandra\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        # os.startfile(os.path.join(songs_dir, songs[0]))   # here 0 => 0 + 1 = 1 => 1st song of the directory/ file
        # os.startfile(os.path.join(songs_dir, songs[1]))   # here 1 => 1 + 1 = 2 => 2nd song of the directory/ file
        random_song = random.choice(songs)
        os.startfile(os.path.join(songs_dir, random_song))

    # Current Time Statement
    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Let me see {MASTER} ..... The time is ... {strTime}")

    # Opening Application/Software
    elif 'open code' in query.lower():
        codePath = "C:\\Users\\steph\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        speak("initializing Work space... Opening Visual studio code")
        print("Opening VS Code...")
        os.startfile(codePath)  # Must have VS Code Installed in Device

    elif 'open telegram' in query.lower():
        telPath = "C:\\Program Files\\WindowsApps\\TelegramMessengerLLP.TelegramDesktop_3.6.0.0_x64__t4vj0pshhgkwm\\Telegram.exe"
        speak("initializing Chat... Opening telegram")
        print("Opening Telegram...")
        os.startfile(telPath)  # Must have Telegram Installed in Device

    elif 'open android studio' in query.lower():
        andstuPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio\\Android Studio.lnk"
        # Must have Android Studio Installed in Device
        speak("initializing Work space... Opening android studio")
        print("Opening Android Studio...")
        os.startfile(andstuPath)

    elif 'open camera' in query.lower():
        camPath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsCamera_2022.2201.4.0_x64__8wekyb3d8bbwe\\WindowsCamera.exe"
        speak("initializing Camera... Opening Camera")
        print("Opening Camera...")
        os.startfile(camPath)

    elif 'open system detail' in query.lower():
        sys_det_Path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\CPUID\\CPU-Z\\CPU-Z.lnk"
        speak("initializing C P U - Z ... Opening System Configurations")
        print("Opening System Detail...")
        os.startfile(sys_det_Path)  # Must have CPU-Z Installed in Device

    elif 'search for a file' in query.lower():
        search_Path = "C:\\Program Files\\Everything\\Everything.exe"
        speak("initializing Everthing...the advance file manager... Opening source to find out any file")
        print("Opening Everthing...")
        os.startfile(search_Path)  # Must have Everything Installed in Device

    elif 'code in java' in query.lower():
        java_Path = "C:\\Users\\steph\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Eclipse\\Eclipse IDE for Java Developers - 2021-06.lnk"
        # Must have Eclipse Installed and Setupped in Device
        speak("initializing work space in Eclipse Integrated development environment... Opening java work space")
        print("Opening Workspace of Java...")
        os.startfile(java_Path)

    elif 'code in python' in query.lower():
        pyt_Path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2021.3.1.lnk"
        # Must have Pycharm Installed and Setupped in Device
        speak("initializing work space in Pycharm Integrated development environment... Opening python work space")
        print("Opening Workspace of python...")
        os.startfile(pyt_Path)

    elif 'code in c' in query.lower():
        turbo_c_Path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\TurboC 7 by Akki\\TurboC 7 by Akki.lnk"
        # Must have Turbo C++ by Installed in Device
        speak("initializing work space in Turbo C plus plus by Akki... Opening i d e for C")
        print("Opening Workspace for C...")
        os.startfile(turbo_c_Path)

    elif 'virtual machine' in query.lower() or 'virtual box' in query.lower():
        VMPath = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
        # Must have Oracle VM VirtualBox Installed and Setupped in Device
        speak("initializing Oracle v m virtual box manager... Opening Virtual machine")
        print("Opening Oracle VM VirtualBox...")
        os.startfile(VMPath)

    elif 'open whatsapp' in query.lower():
        whatsappPath = "C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2208.14.0_x64__cv1g1gvanyjgm\\app\\WhatsApp.exe"
        # Must have WhatsApp Installed and Setupped in Device
        speak("Contacting mark zuckerberg ... Opening whatsapp")
        print("Opening WhatsApp...")
        os.startfile(whatsappPath)

    elif 'attend a meeting' in query.lower():
        zoomPath = "C:\\Users\\steph\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Zoom.lnk"
        # Must have Zoom Installed and Setupped in Device
        speak("Contacting eric yuan ... Opening zoom")
        print("Opening Zoom...")
        os.startfile(zoomPath)

    elif 'open terminal' in query.lower():
        terPath = "C:\\Users\\steph\\AppData\\Local\\Microsoft\\Windows\\WinX\\Group3\\02 - Windows Terminal.lnk"
        speak("Opening Windows terminal...")
        print("Opening Windows Terminal...")
        os.startfile(terPath)

    elif 'open powershell' in query.lower():
        PSPath = "C:\\Users\\steph\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell.lnk"
        speak("Opening windows powershell")
        print("Opening Windows Powershell...")
        os.startfile(PSPath)

    elif 'open command prompt' in query.lower():
        cmdPath = "C:\\Users\\steph\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command Prompt.lnk"
        speak("Trying c m d ... Opening command prompt")
        print("Opening Command Prompt...")
        os.startfile(cmdPath)

    # Open Microsoft Apps
    elif 'open excel' in query.lower():
        excelPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
        speak("Contacting bill gates office ... Opening Microsoft Excel")
        print("Opening Excel...")
        os.startfile(excelPath)

    elif 'open word' in query.lower():
        wordPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
        speak("Contacting bill gates office ... Opening Microsoft word")
        print("Opening Word...")
        os.startfile(wordPath)

    elif 'open powerpoint' in query.lower():
        pptPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
        speak("Contacting bill gates office ... Opening Microsoft Power point")
        print("Opening PowerPoint...")
        os.startfile(pptPath)

    elif 'open access' in query.lower():
        accessPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Access.lnk"
        speak("Contacting bill gates office ... Opening Microsoft Access")
        print("Opening Access...")
        os.startfile(accessPath)

    elif 'open onedrive' in query.lower():
        onedrivePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneDrive.lnk"
        speak("Contacting bill gates office ... Opening Microsoft One drive")
        print("Opening Onedrive...")
        os.startfile(onedrivePath)

    elif 'open onenote' in query.lower():
        onenotePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote.lnk"
        speak("Contacting bill gates office ... Opening Microsoft One note")
        print("Opening OneNote...")
        os.startfile(onenotePath)

    elif 'open outlook' in query.lower():
        outlookPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Outlook.lnk"
        speak("Contacting bill gates office ... Opening Microsoft out look")
        print("Opening OutLook...")
        os.startfile(outlookPath)

    elif 'open publisher' in query.lower():
        publisherPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Publisher.lnk"
        speak("Contacting bill gates office ... Opening Microsoft publisher")
        print("Opening Publisher...")
        os.startfile(publisherPath)

    # Basic Questions
    elif 'how are you' in query:
        speak("I am fine... Glad You asked... Thank you")
        speak("How are you, Sir")

    elif "who made you" in query or "who created you" in query:
        speak("I have been created by Master Stephen Arputharaj")

    elif 'joke' in query:
        speak(pyjokes.get_joke())

    elif "will you be my gf" in query or "will you be my bf" in query:
        speak("I'm not sure about, may be you should give me some time")

    elif "why you came to world" in query:
        speak("Thanks to Stephen. further It's a secret")

    elif "i love you" in query:
        speak("It's hard to understand ... But Im in Love with Edith ... So sorry Master")

    elif "who i am" in query:
        speak("If you talk then definitely your human.")

    elif 'is love' in query:
        speak("It is 7th sense that destroy all other senses")

    elif "who are you" in query:
        speak("I am your Desktop Assistant ... virtual assistant to be specific, created by Stephen Arputharaj")

    elif 'reason for you' in query:
        speak("I was created as a final year ... I mean ... for a third year project ... by Master Stephen Arputharaj ")

    # Opening Speed test app
    elif 'internet speed' in query.lower():
        intspdPath = "C:\\Program Files\\Speedtest\\Speedtest.exe"
        speak("initializing Ookla... Opening Internet speed tester")
        print("Opening Internet Speed Test...")
        os.startfile(intspdPath)

    # Editing softwares
    elif 'edit video' in query.lower():
        davinrePath = "C:\\Users\\steph\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Blackmagic Design\\DaVinci Resolve\\DaVinci Resolve.lnk"
        speak("initializing Black magic design... Opening da vinci resolve")
        print("Opening Da Vinc Resolve...")
        os.startfile(davinrePath)

    elif 'edit music' in query.lower():
        audacityPath = "C:\\ProgramData\\Microsoft\\Windows\\Start\Menu\\Programs\\Audacity.lnk"
        speak("Contacting Dominic Mazzoni and Roger Dannenberg... Opening audacity")
        print("Opening Audacity...")
        os.startfile(audacityPath)

    elif 'edit picture' in query.lower():
        gimpPath = "C:\\Program Files\\GIMP 2\\bin\\gimp-2.10.exe"
        speak("Contacting Spencer Kimball and Peter Mattis... Opening gimp")
        print("Opening Gimp...")
        os.startfile(gimpPath)

    elif 'calculator' in query.lower():
        calciPath = "C:\\Windows\\System32\\calc.exe"
        speak("Oh I see... so You are about do maths... proud of you... Opening Calculator")
        print("Opening Calculator...")
        os.startfile(calciPath)

    elif 'my location' in query:
        from features import My_Location
        My_Location()

    elif 'write a note' in query:
        from automations import Notepad
        Notepad()

    elif 'where is' in query.lower():
        from automations import GoogleMaps
        Place = query.replace("where is ", "")
        Place = Place.replace("sandra", "")
        GoogleMaps(Place)

    # System off Program
    elif 'shutdown system' in query:
        speak("Hold On a Sec ! Your system is on its way to shut down")
        subprocess.call('shutdown / p /f')

    elif "restart" in query:
        speak("Let me wash my face and come ... i mean... i-ll reboot ... Restarting")
        subprocess.call(["shutdown", "/r"])

    elif "hibernate" in query:
        speak("im just closing my eyes...if i don't wake up then do turn on me")
        subprocess.call("shutdown / h")

    elif 'lock window' in query:
        speak("locking the device")
        ctypes.windll.user32.LockWorkStation()

    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])

    elif 'empty recycle bin' in query:
        print("Processing")
        speak(f"Just a second {MASTER} ... in process")
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        print("Recycle Bin Empty")
        speak("You Recycle Bin is now empty as i just deleted everthing inside it forever")

    # Emailing
    elif 'send an email' in query.lower():
        try:
            print("Preparing the essentials that you need...")
            speak("Enter the Email I D to whom you want to send the mail")
            mailid = "Email ID: "
            to = input(mailid)
            print(f"Reaching the Email ID {to}")
            # print(to)
            # to = "email_ID@gmail.com"
            speak("What do you want me to add in content")
            content = takeCommand()
            sendEmail(to, content)
            print("Email Sent Successfully")
            speak("Wow, Your Email has been sent successfully without any issue")
        except Exception as e:
            print(e)

    # elif 'bye' in query.lower():
    #    speak(f"Bye {MASTER} ..... have a great and wonderful day")
    #
    # elif 'bhai' in query.lower():
    #    speak(f"Bye {MASTER} ..... have a great and wonderful day")

    else:
        from Database.ChatBot.ChatBot import ChatterBot
        reply = ChatterBot(query)
        speak(reply)

        if 'bye' in query:
            sys.exit()         # 'break' not working | another option 'return'
        elif 'exit' in query:
            sys.exit()
        elif 'go' in query:
            sys.exit()


main()
