import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import subprocess as sub 
import os
import pyautogui

escuchar = sr.Recognizer()

inicializar = pyttsx3.init()

voices = inicializar.getProperty('voices')
inicializar.setProperty('voice', voices[1].id)

nombre = 'Marta'


sites = {
    'google': 'google.com',
    'youtube': 'youtube.com',
    'github': 'github.com'
}

def habla(texto):
    inicializar.say(texto)
    inicializar.runAndWait()

def tomar():
    try:
        with sr.Microphone() as voz:
            print('Escuchando')
            voice = escuchar.listen(voz)
            command = escuchar.recognize_google(voice, language='es-ES')
            command = command.lower()
            if nombre in command:
                command = command.replace(nombre, " ")
                print(command)

    except:
        pass
    return command


def Marta():
    command = tomar()
    if 'reproduce' in command:
        cancion = command.replace('reproduce','')
        habla('reproduciendo' + cancion)
        pywhatkit.playonyt(cancion)

    elif 'hora' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        habla('Son las' + time)
    elif 'wikipedia' in command:
        busqueda = command.replace('wikipedia', '')
        informacion = wikipedia.set_lang('es')
        informacion = wikipedia.summary(busqueda, 1)
        print(informacion)
        habla(informacion)
    elif "pantalla" in command:
        screenshot = pyautogui.screenshot()
        screenshot.save('Screenshot.png')
        habla('capturando la pantalla')
    else:
        habla('Recuerde decir mi nombre')
        
   
Marta()