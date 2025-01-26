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
engine.setProperty('voice', voices[1].id)

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
    music_dir = r'S:\Pattu_Song' 
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
def open_wikipedia(query):
    speak("What topic would you like to search on Wikipedia?")
    topic = take_command().lower()

    if topic != "none":
        speak(f"Searching Wikipedia for {topic}")
        search_url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
        webbrowser.open(search_url)
        speak(f"I've opened Wikipedia for {topic}.")
    else:
        speak("Sorry, I didn't catch that. Please try again.")
            
def open_youtube(query):
    speak("What song would you like me to play?")
    song_name = take_command().lower()
    
    if song_name != "none":
        speak(f"Searching YouTube for {song_name}")
        search_url = f"https://www.youtube.com/results?search_query={song_name}"
        webbrowser.open(search_url)
        speak("The search page is now open. Please say the number of the video you want to play (e.g., 'play 1', 'play 2').")
        
        while True:
            video_number_query = take_command().lower()
            video_number = None
            for ordinal, num in range(1,5):
                if ordinal in video_number_query:
                    video_number = num
                    break
                if not video_number:
                    video_number = 1
                video_url = f"https://www.youtube.com/watch?v={video_number}"
            try:
                webbrowser.open(video_url)
                speak(f"Now playing video {video_number}.")
                break
            except Exception as e:
                speak("Sorry, I wasn't able to open the video. Please try again.")
                print(f"Error: {e}")       
        while True:
            query = take_command().lower()
            if 'yes' in query:
                speak("Please say the number of the video you want to play.")
                break
            elif 'no' in query:
                speak("Goodbye. Have a nice day!")
                return
            else:
                speak("Sorry, I didn't catch that. Please say 'yes' to play another video or 'no' to stop.")
    else:
        speak("Sorry, I didn't catch that. Please try again.")
def open_amazon():
    speak("Opening Amazon.")
    webbrowser.open("https://www.amazon.com")

def open_flipkart():
    speak("Opening Flipkart.")
    webbrowser.open("https://www.flipkart.com")
        
music_dir = r'S:\testingsong'

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            open_wikipedia(query)
            
        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query or 'play song' in query:
            play_music()
            
        elif 'open youtube' in query:
            open_youtube(query)
            
        elif 'amazon' in query:
            open_amazon()

        elif 'flipkart' in query:
            open_flipkart()
            
        elif 'exit' in query:
            speak("Goodbye. Have a nice day!")
            break