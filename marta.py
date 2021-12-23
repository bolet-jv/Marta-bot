import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import subprocess as sub 
import os

name = 'Marta'
listener =  sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


sites={
          'google': 'google.com',
          'youtube': 'youtube.com',
          'gmail': 'mail.google.com',
          }





def talk(text):
  engine.say(text)
  engine.runAndWait()


def listen():
    try:
      with sr.Microphone() as source:
        print('Escuchando...')
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        rec = rec.lower()
        if name in rec:
            rec = rec.replace(name, '')
        print(rec)

    except:
      pass
    return rec

def run():
   while True:
    rec = listen()
    if'play' in rec:
     music = rec.replace('play', '')
     talk('Playing'+ music )
     pywhatkit.playonyt(music)
    elif 'time' in rec:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('its'+ time)
    elif 'search'in rec:
        order = rec.replace('search', '')
        info = wikipedia.summary(order, 1)
        talk(info)
    elif 'open' in rec:
        for site in sites:
            if site in rec:
                sub.call(f'start chrome.exe {sites[site]}', shell=True)
                talk(f'opening {site}')
    elif 'write' in rec:
        try:
            with open("nota.txt", 'a') as f:
                write(f)
        except FileNotFoundError as e:
            file = open("nota.txt", 'a')
            write(file)
    elif 'finish' in rec:
        talk('Byee, Dave!')  
        break
           

    else :
        talk("Try Again, Dave")
    

def write(f):
    talk("What do you want me to write, Dave")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("You can check now, Dave")
    sub.Popen("nota.txt", shell=True)

run()