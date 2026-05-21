# Medium Article Reader

Scrapes an article from a URL, summarizes it with an OpenAI LLM via LangChain, and reads the summary or full text aloud with text-to-speech.

## How to run

```
pip install pyttsx3 requests beautifulsoup4 openai python-dotenv langchain
python main.py
```

Requires an OpenAI API key in a `.env` file.

## Dependencies

pyttsx3, requests, beautifulsoup4, openai, python-dotenv, langchain.

## Pyodide-runnable
No — it makes live HTTP/API requests and uses pyttsx3 text-to-speech.
