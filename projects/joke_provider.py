import speech_recognition as sr
import pyttsx3
import requests


# Obtaining the response from the api after sending the request of a triggered word
def get_joke():
    api_url = "https://api.openai.com/v1/engines/davinci-codex/completions"  # provide the api key
    prompt = "Tell me a joke"

    response = requests.post(
        api_url,
        json={"prompt": prompt},
        headers={"Authorization": "Bearer YOUR_API_KEY"},
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return "Sorry, I couldn't come up with a joke right now."


# Speaking the output or joke
def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voices", voices[0].id)
    engine.setProperty("rate", 170)
    engine.say(Text)
    engine.runAndWait()


# Initialize the recognizer
r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1  # taking the input from the user
            audio = r.listen(source, 0, 8)

        query = r.recognize_google(audio)
        if "tell me a joke" in str(query).lower():  # making a specific triggered word
            joke = get_joke()
            print("Here's a joke:", joke)

            # Convert text to speech and play it
            Speak(joke)

    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
    except KeyboardInterrupt:
        print("Exiting the program.")
        break
    # releasing the resources
