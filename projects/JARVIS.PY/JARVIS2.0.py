# Importing necessary modules
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes  # pip install jokes

# Initializing speech synthesis engine
Listener = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    # Function to speak the given text
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    # Function to greet the user based on the time of day
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("jarvis here at your service sir. How may I help you?")


def takeCommand():
    # Function to listen to user's voice input and return the recognized text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # If speech recognition fails, prompt the user to repeat the command
        print("Could you please repeat it, sir...")
        return "None"
    return query


def sendEmail(to, content):
    # Function to send an email using the provided email credentials
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-password")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # Exits the interpreter if you just say quit or exit
        if query == "quit" or query == "exit":
            break
        # Logic for executing tasks based on user's query
        if "wikipedia" in query:
            # Searching and reading information from Wikipedia
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            # Open YouTube in the default web browser
            webbrowser.open("youtube.com")

        elif "open google" in query:
            # Open Google in the default web browser
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            # Open Stack Overflow in the default web browser
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            # Play music from the specified directory
            music_dir = "D:\\Non Critical\\songs\\Favorite Songs2"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            # Get and speak the current time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            # Open Microsoft Visual Studio Code
            codePath = "C:\\Users\\your desktop\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "email to Raj" in query:
            # Compose and send an email
            try:
                speak("What should I say, sir?")
                content = takeCommand()
                to = "yourmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent, sir!")
            except Exception as e:
                print(e)
                speak("Sorry, boss. I am not able to send this email.")

        elif "are you single" in query:
            # Respond humorously to the question about being single
            speak("I am in a relationship with wifi")

        elif "joke" in query:
            # Tell a random joke
            speak(pyjokes.get_joke())
else:
    # If the user's query doesn't match any defined tasks, ask for the command again
    speak("Please say the command again, sir.")
