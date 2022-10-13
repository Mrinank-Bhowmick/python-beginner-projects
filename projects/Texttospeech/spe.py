def speccecc():
    import speech_recognition as sr
    from gtts import gTTS
    import pyglet
    import time,os
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        print("done")
    try:
        text=r.recognize_google(audio)
        print("You said " + text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    return text
