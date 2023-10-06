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


import logging
import sys
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters)

from cryptotrackerbot import commands


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))


def main():
    if len(sys.argv) == 2:
        bot_token = sys.argv[1]
    else:
        print("\n!WARNING!:\nadd the bot token as paramter when running the bot.\nExiting...")
        sys.exit(0)

    print("\nrunning...")
    # define the updater
    updater = Updater(token=bot_token, workers=10)
    
    # define the dispatcher
    dp = updater.dispatcher

    # commands
    dp.add_handler(CommandHandler(('price', 'p'), commands.price_command, pass_args=True, pass_job_queue=True))
    dp.add_handler(CommandHandler(('start', 'help'), commands.help, pass_job_queue=True))
    dp.add_handler(CommandHandler(('rank', 'r'), commands.rank_command, pass_job_queue=True))
    dp.add_handler(CommandHandler(('graph', 'g'), commands.graph_command, pass_args=True, pass_job_queue=True))


    # handle errors
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
