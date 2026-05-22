# Medium Article Reader

Scrapes an article from a URL, summarizes it with an OpenAI LLM via LangChain, and reads the summary or full text aloud with text-to-speech.

## Example

```text
Paste article URL: https://medium.com/some-article
This article discusses the rise of renewable energy and its impact on global
power markets, highlighting solar adoption trends and policy developments...
Enter 1 for summary of article or Enter 2 for whole article: 1
(text-to-speech reads the summary aloud)
```

## How to run on localhost

```
pip install pyttsx3 requests beautifulsoup4 openai python-dotenv langchain
python main.py
```

Requires an OpenAI API key in a `.env` file.

## Dependencies

pyttsx3, requests, beautifulsoup4, openai, python-dotenv, langchain.
