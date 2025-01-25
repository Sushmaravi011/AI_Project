import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
from playsound import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your assistant, How can I assist you?")

def take_command():
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
        print("Say that again please...")
        speak("Sorry, I didn't understand that. Could you say that again?")
        return "None"
    return query

def play_song(song_path):
    try:
        print(f"Playing song from: {song_path}")
        os.system(f"start wmplayer \"{song_path}\"")
    except Exception as e:
        print(f"Error playing the song: {e}")
        speak(f"There was an error while trying to play the song: {e}")

def play_music():
    speak("What song would you like me to play?") 
    music_dir = r'S:\testingsong' 
    songs = os.listdir(music_dir)
    
    while True:
        query = take_command().lower()
        
        if 'exit' in query or 'stop' in query:
            speak("Stopping music. Goodbye!")
            break 

        if 'random' in query:
            song_to_play = random.choice(songs)
        else:
            song_name = query.replace('play music', '').strip()
            matched_songs = [song for song in songs if song_name.lower() in song.lower()]

            if matched_songs:
                song_to_play = matched_songs[0] 
            else:
                speak("Sorry, I couldn't find that song. Playing a random song instead.")
                song_to_play = random.choice(songs)  
        song_path = os.path.join(music_dir, song_to_play)  
        print(f"Playing: {song_to_play}")
        play_song(song_path)  

        speak("Would you like me to play another song?")
        query = take_command().lower()
        if 'no' in query or 'stop' in query:
            speak("Goodbye! Stopping the music.")
            break
        elif 'yes' not in query:
            speak("Sorry, I didn't catch that. Please say 'yes' to play another song or 'no' to stop.")


music_dir = r'S:\testingsong'

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("What song would you like me to play?")
            song_name = take_command().lower()
            if song_name != "none":
                speak(f"Searching YouTube for {song_name}")
                search_url = f"https://www.youtube.com/results?search_query={song_name}"
                webbrowser.open(search_url)
            else:
                speak("Sorry, I didn't catch that. Please try again.")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")
            
        elif 'exit' in query:
            speak("Goodbye. Have a nice day!")
            break

        elif 'play music' in query or 'play song' in query:
            play_music() 