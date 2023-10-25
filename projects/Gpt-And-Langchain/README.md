# OpenAI and Langchain

## Table of Contents
+ [About](#about)
+ [Getting Started](#getting_started)

## About <a name = "about"></a>
Is LangChain using OpenAI?
Generative AI Applications with LangChain and OpenAI API
LangChain offers an OpenAI chat interface to call the model APIs into your application and create a question/answer pipeline that answers users' queries based on given context or input documents. It basically performs a vectorized search to find the most similar answer to the question

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites
* activate venv in local system
```
.\.venv\Scripts\activate
```
* install requirements for code to run
```
pip  install -r requirements.txt
```
## API Documentation
### Get API KEY from [**Telegram Bot**]('https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/')
### Get API KEY from [**OPenAI**]('https://platform.openai.com/account/api-keys')
### Get API KEY from [**Notion Database**]('https://thienqc.notion.site/Notion-API-Python-ca0fd21bc224492b8daaf37eb06289e8')
### Get API KEY from [**Serapi**]('https://serpapi.com/search-api')

* Reference youtube link for How to get [**API key**](https://www.youtube.com/watch?v=ytNyibPQFhw)
* Create .env file for apikey

```
BOT_TOKEN= 'Telegram Bot Token'
OPENAI_API_KEY = 'API Key'
NOTION_TOKEN = 'Notion Token'
DATABASE_ID = 'Notion Database ID'
SERPAPI_API_KEY = 'SERP API Key'
```

### Runnning in local Host
```
py telegram-bot.py
```



