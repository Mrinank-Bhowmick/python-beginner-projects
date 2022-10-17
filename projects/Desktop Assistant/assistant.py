"""

"""
import pyttsx3                   #for text to speech conversion.
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
import json
engine=pyttsx3.init('sapi5')               #sapi5 is a tool by microsoft for speech recognition
voices=engine.getProperty('voices')
print(voices[1].id)      #0 will be the voice of boy David & 1 will be the voice of girl Hazel
engine.setProperty('voice',voices[1].id)


def utter(audio):
    engine.say(audio)
    engine.runAndWait()

def covid():
    from covid import Covid
    covid=Covid()
    cases=covid.get_status_by_country_name("India")
    for x in cases:
        print(x,":",cases[x])

def tell(str):                   #we have to define this so that our siri can tell us the news
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

def input():
    """#it takes input from microphone (user) and returns string output"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source,duration=3)
        audio=r.listen(source)

    try:
        print("Recognising....")
        inquire=r.recognize_google(audio,language='en-in')   #using google for voice recognition
        print(f"User Said: {inquire}\n")


    except Exception as e:
        #print(e)                              #this will print exception but instead of it we are making it print ry Saying Out Again Please.....
        print("Try Saying Out Again Please.....")    #Try Saying Out Again Please..... will get printed incase of improper voice
        return "None"             #none here is simply a string
    return inquire


if __name__=='__main__':            #this is used to call our function
    input()
    while (True):
        inquire=input().lower()
           #logic for executing task based on inquire
        if 'hi siri' in inquire:
            print("Hi! , How Can I Help")
            utter("Hi! , How Can I Help")

        if 'hi what is your name' in inquire:
            print("Hello Sir , My Name iS Siri")
            utter("Hello Sir , My Name iS Siri")

        if 'who created you' in inquire:
            print("Prakar Sinha Has Created Me")
            utter("Prakar Sinha Has Created Me")

        if 'what can you do' in inquire:
            print("i can do many things like speak out news for you , play music for you , can search famous celebrity on wikipedia and many more")
            utter("i can do many things like telling you news , play music for you , can search famous celebrity on wikipedia and many more")

        if 'covid-19' in inquire:
            utter("Here is the details of covid 19 in India")
            print(covid())

        if 'wikipedia' in inquire:
            utter("Searching Wikipedia")
            inquire=inquire.replace("wikipedia","")
            results=wikipedia.summary(inquire,sentences=2)     #we can change the value of sentences as per the need
            utter("According To Wikipedia")
            print(results)                                   #to print whatever it is uttering
            utter(results)

        if 'open amazon' in inquire:
            webbrowser.open("amazon.com")
            utter("opening amazon")
            print("opening amazon")

        if 'open google' in inquire:
            webbrowser.open("Google.com")
            utter("opening google")
            print("opening google")

        if 'open hackerrank' in inquire:
            webbrowser.open("HackerRank.com")
            utter("opening hackerrank")
            print("opening hackerrank")

        if 'play music' in inquire:
            music_dir='C:\\music'            #double slash(\\) is used for escaping
            music=os.listdir(music_dir)      #os.listdir help us to get all songs from that directory
            print(music)
            os.startfile(os.path.join(music_dir,music[0]))       #0 is used so that we can hear the first song

        if 'what is the time' in inquire:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            utter(f"Sir The Time iS {strTime}")

        if 'tech news' in inquire:
            tell("Latest News")
            url = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=a9ee52ae8d4d4d7aa8115a868ff40393"
            news = requests.get(url).text
            news_dict = json.loads(news)  # loads convert strings to python projects as json.loads takes strings value
            print(news_dict["status"])  # output is coming ok because status is OK in the original js file.
            headlines = news_dict['articles']
            for article in headlines:
                tell(article['title'])
                tell("Lets Move On To the next news")
            tell("Thanks For Listening")


        if 'ok bye' in inquire:
            print("Okay Bye Sir , i M Glad You Talked Me")
            utter("Okay Bye Sir , i M Glad You Talked Me")
            break