# Voice_Assistant-2.0-

Disclaimer:
The code in this repository is the original work of Ridshabh Patel or feristof . Any use or reproduction of this code must give proper credit by tagging my name and links and including a link to this repository. 

In this project, the following libraries and modules were used:

speech_recognition for speech recognition
gTTS for text-to-speech conversion
pygame for playing audio files
os for interacting with the operating system
random for generating random numbers
webbrowser for opening web pages
time for timing operations
geopy.geocoders for geographic location information
wikipediaapi for accessing Wikipedia information
pyautogui for automating GUI interactions
Please note that these modules need to be installed prior to running the code.



Here is a list of the functions and calls used in this project and their purpose:

speech_recognition.Recognizer() - initializes the speech recognizer
sr.Microphone() - initializes the microphone for speech input
sr.listen() - listens for speech input
sr.recognize_google() - uses Google's speech recognition service to recognize speech
gTTS(text, lang='en') - converts text to speech using Google's TTS service
pygame.init() - initializes pygame
pygame.mixer.music.load() - loads an audio file for playback
pygame.mixer.music.play() - plays the loaded audio file
os.system() - runs a command in the operating system
random.randint() - generates a random integer
webbrowser.open() - opens a web page in the default browser
time.sleep() - pauses the program for a specified amount of time
geopy.geocoders.Nominatim() - initializes the geolocator
geolocator.geocode() - gets the location information for a given address
wikipediaapi.Wikipedia() - initializes the Wikipedia API
wikipedia.page() - gets a Wikipedia page for a given topic
pyautogui.press() - simulates a key press
pyautogui.typewrite() - simulates typing