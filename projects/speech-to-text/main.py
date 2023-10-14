import speech_recognition
import pyttsx3


# initializing the recognizer object
recognizer =  speech_recognition.Recognizer()
while True:

    try:
        # using microphone as input here
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic,duration=0.2)

            # listen to the microphone
            audio = recognizer.listen(mic)
            
            # using google speech recognition API for recognition
            text = recognizer.recognize_google(audio)
            text=text.lower()
            
            print(f"Recognized text : {text}")
            
    except speech_recognition.UnknownValueError():
        # If there's an interrupt or some kind of error start from the beginning and initialise the recognizer again
        recognizer =  speech_recognition.Recognizer()
        continue
