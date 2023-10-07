import pyttsx3
import requests
import os
from bs4 import BeautifulSoup
import openai
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain

load_dotenv()
openai_api_key = os.getenv("API_KEY")
openai.openai_api_key = openai_api_key

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


try:
    text = input("Paste article URL: ")

    ## scraping from URL
    res = requests.get(text)
    soup = BeautifulSoup(res.text, "html.parser")
    articles = []
    for p in soup.select("p"):
        article = p.getText().strip()
        articles.append(article)
    txt = " ".join(articles)

    ## loading text from URL for summarizing..
    loader = WebBaseLoader(text)
    docs = loader.load()
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo-16k",
        openai_api_key=openai.openai_api_key,
    )
    chain = load_summarize_chain(llm, chain_type="stuff")
    print(chain.run(docs))

    user_choice = int(
        input("Enter 1 for summary of article or Enter 2 for whole article: ")
    )
    if user_choice == 1:
        speak(chain.run(docs))
    else:
        speak(txt)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
