import telebot
from telebot import types

bot = telebot.TeleBot("6540560961:AAEuobp6IGekPHPwSDxbxEEgI9LbPvYRgEc")


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    note = types.KeyboardButton("Добавить заметку")
    deletenote = types.KeyboardButton("Удалить заметку")
    editnote = types.KeyboardButton("Изменить заметку")
    event = types.KeyboardButton("Добавить событие")
    deletevent = types.KeyboardButton("Удалить событие")
    editevent = types.KeyboardButton("Изменить событие")
    check = types.KeyboardButton("Открыть текущие заметки/события")
    keyboard.add(note, deletenote, editnote, event, deletevent, editevent, check)
    bot.send_message(
        message.chat.id,
        f"<b>{message.from_user.first_name}, я так рад, что вы снова сдесь!</b> \U0001F601 \nВыберите, что бы вы хотели сделать:",
        parse_mode="html",
        reply_markup=keyboard,
    )


@bot.message_handler(func=lambda message: True)
def handle_button_click(message):
    if (message.text.lower() == "добавить заметку") or (
        message.text.lower() == "/addn"
    ):
        addn(message)
    elif (message.text.lower() == "добавить событие") or (
        message.text.lower() == "/adde"
    ):
        adde(message)
    elif (message.text.lower() == "удалить заметку") or (
        message.text.lower() == "/deleten"
    ):
        deleten(message)
    elif (message.text.lower() == "удалить событие") or (
        message.text.lower() == "/deletev"
    ):
        deletev(message)
    elif (message.text.lower() == "изменить заметку") or (
        message.text.lower() == "/editn"
    ):
        editn(message)
    elif (message.text.lower() == "изменить событие") or (
        message.text.lower() == "/edite"
    ):
        edite(message)
    elif (message.text.lower() == "открыть текущие заметки/события") or (
        message.text.lower() == "/check"
    ):
        check(message)
    elif message.text == "/help":
        bot.send_message(
            message.chat.id,
            "<b>С моей помощью вы легко сможете:</b>\n\n"
            "<b>1)</b> Добавить для себя любую заметку коммандой - | /addn |\n\n"
            "<b>2)</b> Создать событие с напоминанием коммандой - | /adde |\n\n"
            "<b>3)</b> Удалить любую заметку коммандой - | /deleten |\n\n"
            "<b>4)</b> Удалить любое событие коммандой - | /deletev |\n\n"
            "<b>5)</b> Изменить любую заметку коммандой - | /editn |\n\n"
            "<b>6)</b> Изменить любое событие коммандой - | /edite |\n\n"
            "<b>7)</b> Просматривать все свои заметки коммандой - | /check |\n\n",
            parse_mode="html",
        )
    elif message.text.isalpha():
        bot.send_message(
            message.chat.id,
            "Извини, но я не воспринимаю текст \U0001F972, тебе следует попробовать комманды!\n"
            "Чтобы узнать, что я умею, введи комманду - | /help |",
        )
    elif message.text.isdigit():
        bot.send_message(
            message.chat.id,
            "Извини, но я не воспринимаю цифры/числа \U0001F972, тебе следует попробовать комманды!\n"
            "Чтобы узнать, что я умею, введи комманду - | /help |",
        )
    else:
        bot.send_message(
            message.chat.id,
            "Извини, но я воспринимаю только комманды \U0001F972\n"
            "Чтобы узнать, что я умею, введи комманду - | /help |",
        )


def addn(message):
    bot.send_message(message.chat.id, "Вы создали заметку")


def adde(message):
    bot.send_message(message.chat.id, "Вы создали событие")


def deleten(message):
    bot.send_message(message.chat.id, "Вы хотите удалить заметку")


def deletev(message):
    bot.send_message(message.chat.id, "Вы удалили событие")


def editn(message):
    bot.send_message(message.chat.id, "Вы хотите изменить заметку")


def edite(message):
    bot.send_message(message.chat.id, "Вы хотите изменить событие")


def check(message):
    bot.send_message(message.chat.id, "Вы хотите посмотреть список заметок/событий")


bot.polling(none_stop=True)
