import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
recognizer = sr.Recognizer()
text_to_speech = pyttsx3.init()
def listen_to_audio():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio).lower()
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error connecting to the Google API.")
        return ""

def speak(text):
    text_to_speech.say(text)
    text_to_speech.runAndWait()
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
def handle_commands(command):
    if "wikipedia" in command:
        search_query = command.replace("wikipedia", "")
        result = wikipedia.summary(search_query, sentences=2)
        speak("According to Wikipedia:")
        speak(result)
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
    elif "open anime" in command:
        webbrowser.open("https://animesuge.to/home")
    elif "open spotify" in command:
        webbrowser.open("https://www.spotify.com/")
    elif "open google" in command:
        webbrowser.open("https://www.google.com/")
    elif "play video" in command:
        music_dir = "D:\song"
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak("No music files found in the directory.")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")
    
    else:
        speak("I'm sorry, I'm not sure how to respond to that.")

def virtual_assistant():
    greet()
    speak("How can I assist you today?")
    while True:
        user_input = listen_to_audio()
        handle_commands(user_input)

if __name__ == "__main__":
    virtual_assistant()
