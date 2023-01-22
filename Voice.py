import speech_recognition as sr
from gtts import gTTS
import pygame
import os
import random
import webbrowser
import time
from geopy.geocoders import Nominatim
import wikipediaapi
import pygame
import pyautogui


def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Say something!")
        audio = r.listen(source)
    try:
        # recognize speech using Google Speech Recognition
        text = r.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said.")
        listen()
    except sr.RequestError as e:
        speak("Sorry, there was an error in the request. Please try again.")
        listen()



def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    pygame.quit()
    os.remove("response.mp3")


def search_web(query):
    speak("Searching the web for " + query)
    webbrowser.open("https://www.google.com/search?q=" + query)

def get_time_date(query):
    current_time = time.strftime("%H:%M:%S", time.gmtime())
    current_date = time.strftime("%Y-%m-%d", time.gmtime())
    if "time" in query or "what time is it" in query or "what's the time" in query:
        speak("The current time is " + current_time)
    elif "date" in query or "what date is it" in query or "what's the date" in query:
        speak("The current date is " + current_date)
    else:
        speak("I'm sorry, I didn't understand if you wanted the time or the date.")

def get_location(query):
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(query)
    speak("The location of " + query + " is " + location.address)
    webbrowser.open("https://www.google.com/maps/place/" + location.address)


def get_wiki(query):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(query)
    speak("The summary of " + query + " is " + page_py.summary)

import pyautogui

def play_music(query):
    speak("Playing " + query)
    webbrowser.open("https://www.youtube.com/results?search_query=" + query)
    time.sleep(2)  # wait for the page to load
    pyautogui.press("enter")  # press the Enter key to play the first video



while True:
    query = listen().lower()
    if "hello" in query:
        speak("Hello, how can I help you today?")
    elif "goodbye" in query:
        speak("Goodbye, have a nice day.")
        break
    elif "time" in query or "date" in query:
        get_time_date(query)
    elif "location" in query:
        query = query.replace("location", "")
        get_location(query)
    elif "wikipedia" in query:
        query = query.replace("wikipedia", "")
        get_wiki(query)
    elif "play" in query:
        query = query.replace("play", "")
        play_music(query)
    elif "search" in query:
        query = query.replace("search", "")
        search_web(query)
    else:
        speak("I'm sorry, I didn't understand what you said.")

