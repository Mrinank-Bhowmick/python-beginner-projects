# CryptoTrackerBot - check cryptocurrencies prices on telegram
# Copyright (C) 2018  Dario 91DarioDev <dariomsn@hotmail.it> <github.com/91dariodev>
#
# CryptoTrackerBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CryptoTrackerBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with CryptoTrackerBot.  If not, see <http://www.gnu.org/licenses/>.


from telegram.ext.dispatcher import run_async

import datetime
import io
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
from matplotlib.dates import date2num
from PIL import Image

from matplotlib import ticker
import matplotlib.dates as mdates
from matplotlib.finance import candlestick_ohlc

from telegram.ext.dispatcher import run_async
from telegram.error import BadRequest
from cryptotrackerbot import emoji

matplotlib.use('Agg')


@run_async
def send_autodestruction_message(bot, update, job_queue, text, parse_mode='HTML', 
                                destruct_in=20, quote=False, disable_web_page_preview=True):
    if update.effective_chat.type == "private":
        update.message.reply_text(text, parse_mode=parse_mode, disable_web_page_preview=disable_web_page_preview)
    else:
        message_id = update.message.reply_text(text, parse_mode=parse_mode, quote=quote, 
                                                disable_web_page_preview=disable_web_page_preview).message_id
        chat_id = update.effective_chat.id
        command_id = update.message.message_id
        job_queue.run_once(
            destruction, 
            destruct_in, 
            context=[chat_id, command_id, message_id]
        )


@run_async
def send_autodestruction_photo(bot, update, pic, caption, job_queue, 
                                destruct_in=60, quote=False):
    if update.effective_chat.type == "private":
        bot.sendChatAction(chat_id=update.effective_chat.id, action='UPLOAD_PHOTO')
        bot.send_photo(chat_id=update.effective_chat.id, photo=pic, caption=caption)
    else:
        bot.sendChatAction(chat_id=update.effective_chat.id, action='UPLOAD_PHOTO')
        message_id = bot.send_photo(chat_id=update.effective_chat.id, photo=pic, caption=caption).message_id
        chat_id = update.effective_chat.id
        command_id = update.message.message_id
        job_queue.run_once(
            destruction, 
            destruct_in, 
            context=[chat_id, command_id, message_id]
        )


@run_async
def destruction(bot, job):
    chat_id = job.context[0]
    msgs_to_destruct = [job.context[1], job.context[2]]
    for msg in msgs_to_destruct:
        try:
            bot.deleteMessage(chat_id=chat_id, message_id=msg)
        except BadRequest:
                pass


@run_async
def send_sending_photo_alert(bot, update):
    bot.sendChatAction(chat_id=update.effective_chat.id, action='UPLOAD_PHOTO')


def sep(num, none_is_zero=False):
    if num is None:
        return 0 if none_is_zero is False else None
    return "{:,}".format(num)


def arrow_up_or_down(value):
    return emoji.GREEN if value >= 0 else emoji.RED


def string_to_number(string):
    number = string.replace(',', '')
    try:
        number = int(number)
    except ValueError:
        number = float(number)
    return number



def build_graph(ohlc, title=''):
    fig = pyplot.figure(figsize=(15, 7.5))
    ax1 = fig.add_subplot(111)

    for i in ohlc:
        i['time'] = date2num(datetime.datetime.fromtimestamp(i['time']))
    candel_width = (2/3) * (ohlc[1]['time'] - ohlc[0]['time'])
    data = []
    for i in ohlc:
        sub_lst = i['time'], i['open'], i['high'], i['low'], i['close']
        data.append(sub_lst)
    candlestick_ohlc(ax1, data, width=candel_width, colorup='g', colordown='r')
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m %H:%M'))
    ax1.xaxis.set_major_locator(ticker.MaxNLocator(10))
    ax1.grid(True)

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Price')
    ax1.set_title(title)
    ax1.autoscale_view()
    fig.tight_layout()
    fig.autofmt_xdate()

    #pyplot.show()  # no need to call show on server

    bio = io.BytesIO()
    bio.name = "test.png"
    fig.savefig(bio, format='png')
    pyplot.close()  # important to free memory
    bio.seek(0)
    return bio
