import speech_recognition as sr
from googletrans import Translator


# obtain audio from the microphone
def Listen():  # initializing funtion for voice to text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        # setting threshhold frequency for better output
        r.pause_threshhold = 1
        audio = r.listen(source, 0, 8)

    # recognize speech using google
    try:
        print("Recognising")
        query = r.recognize_google(audio, language="en")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error Occured; {0}".format(e))
    except:
        return ""
    query = str(query).lower()  # converting the query into string
    return query


# printing the desired voice input into required text output
print(Listen())
