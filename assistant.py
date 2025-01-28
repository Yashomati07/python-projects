Importing the required libraries :

import speech_recognition as sr 
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser



Initiating the engines for performing text to speech & speech to text :

engine=pyttsx3.init()

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


recognizer=sr.Recognizer()



Declaring the function for recognizing the voices using speech_recognition library :

def cmd():

    with sr.Microphone() as source:

        print("Clearing background noises...Pleasw wait")

        recognizer.adjust_for_ambient_noise(source,duration=0.5)

        print('Ask me anything..')

        recordedaudio=recognizer.listen(source)

    try:

        text=recognizer.recognize_google(recordedaudio,language='en_US')

        text=text.lower()

        print('Your message:',format(text))



    except Exception as ex:


        print(ex)



Inserting the commands to your voice assistant and logics building

 if 'chrome'in text:

        a='Opening chrome..'

        engine.say(a)

        engine.runAndWait()

        programName = "chrome.exe"

        subprocess.Popen([programName])

    if 'time' in text:

        time = datetime.datetime.now().strftime('%I:%M %p')

        print(time)

        engine.say(time)

        engine.runAndWait()

    if 'play' in text:

        a='opening youtube..'

        engine.say(a)

        engine.runAndWait()

        pywhatkit.playonyt(text)

    if 'youtube' in text:

        b='opening youtube'

        engine.say(b)

        engine.runAndWait()


        webbrowser.open('www.youtube.com')



Looping this function:

while True:


    cmd()