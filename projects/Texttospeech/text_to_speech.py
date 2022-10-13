def speechis(mytext,language):
    from gtts import gTTS
    import os
    language = language
    myobj = gTTS(text= mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("welcome.mp3")
def speechis1(mytext,language):
    from gtts import gTTS
    import os
    language = language
    myobj = gTTS(text= mytext, lang=language, slow=False)
    myobj.save("welcome1.mp3")
    os.system("welcome1.mp3")
def speechis2(mytext,language):
    from gtts import gTTS
    import os
    language = language
    myobj = gTTS(text= mytext, lang=language, slow=False)
    myobj.save("welcome2.mp3")
    os.system("welcome2.mp3")
