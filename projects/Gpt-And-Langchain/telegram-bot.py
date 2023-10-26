import os
from dotenv import load_dotenv
from chatbot import LLMPromptTemplate
import telebot

# from chatbot import get_message
# from huggingface import usermessage
from notion import createPage

load_dotenv()
# Getting value form .env
BOT_TOKEN = os.getenv("BOT_TOKEN")


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(func=lambda msg: True)
# def usermessages(message):
#     print(message.text)
#     message1 = usermessage(message.text)
#     bot.reply_to(message, message1)


@bot.message_handler(commands=["Notion"])
def notion(message):
    # message2 = usermessage(message.text)
    text = "split differnet data with *,*"
    # bot.reply_to(message, message2)
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, AddNotion)


def AddNotion(message):
    # message = message.text

    message = message.text
    # message = message.split(",")
    # title, youtube_url, blog_url = message[0], message[1], message[2]
    title = LLMPromptTemplate(message, 1)
    youtube_url = LLMPromptTemplate(message, 2)
    # bot.register_next_step_handler(title,youtube_url, blog_url,)
    message = createPage(title, youtube_url)


bot.infinity_polling()
