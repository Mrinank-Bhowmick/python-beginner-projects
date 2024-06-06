# Scrapes word of the day from dictionary.com

import urllib.request as req
from bs4 import BeautifulSoup
from gtts import gTTS
import os, sys


def get_soup(URL):
    response = req.urlopen(URL)
    data = response.read()
    soup = BeautifulSoup(data, "html.parser")
    response = req.urlopen(URL)
    data = response.read()
    return data


def get_word(data):
    soup = BeautifulSoup(data, "html.parser")
    word_section = soup.find_all("div", {"class": "definition-header"})
    wordOfTheDay = word_section[0].strong.string
    print("Word of the day is: " + wordOfTheDay)
    return wordOfTheDay
    # get_TTS(wordOfTheDay)


def get_word_meanings(data, word):
    soup = BeautifulSoup(data, "html.parser")
    allListOfDetails = soup.find_all("ol")
    listOfDetails = allListOfDetails[0].find_all("li")
    index = 1
    print("Fetching all meanings of the word: " + word)
    for ele in listOfDetails:
        print(str(index) + ". " + ele.span.text)
        index = index + 1


def get_TTS(word):
    print("Generating text-to-speech for " + word + "\n ")
    print("Check current directory where script resides.")
    path = os.getcwd()
    my_tts = word
    tts = gTTS(text=my_tts, lang="en", slow=False)
    tts.save(path + "/" + word + ".mp3")
    try:
        os.system(path + "/" + word + ".mp3")
    except Exception as e:
        print("No software found for running .mp3 file")


def get_more_details(word):
    print("Opening url with word details..")
    word_url = "http://www.dictionary.com/browse/" + word
    if sys.platform == "win32":
        os.startfile(word_url)
    elif sys.platform == "darwin":
        subprocess.Popen(["open", word_url])
    else:
        try:
            subprocess.Popen(["xdg-open", word_url])
        except OSError:
            print("Please open a browser on: " + word_url)


def main():
    URL = "http://www.dictionary.com/wordoftheday/"

    data = get_soup(URL)
    word = get_word(data)
    choice = int(
        input("Do you want to know the meanings of the word ? Press 1.. else Press 0\n")
    )
    if choice == 1:
        get_word_meanings(data, word)
    else:
        pass
    print("\n")
    choice = int(
        input(
            "Do you want to know how the word is pronounced ? Press 1.. else Press 0\n"
        )
    )
    if choice == 1:
        get_TTS(word)
    else:
        pass
    print("\n")
    choice = int(
        input("Do you want to know more about the word ? Press 1.. else Press 0\n")
    )
    if choice == 1:
        get_more_details(word)
    else:
        pass


if __name__ == "__main__":
    main()
