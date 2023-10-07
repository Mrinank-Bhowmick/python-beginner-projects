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

import requests


def get_price(coins): 
    base = "https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms=BTC,USD,EUR"
    upper_coins = [coin.upper() for coin in coins]
    string = ",".join(upper_coins)
    response = requests.get(base.format(string)).json()
    return response


def get_rank(limit=10):
    base = "https://api.coinmarketcap.com/v1/ticker/?limit={}"
    response = requests.get(base.format(limit)).json()
    return response


def get_history(coin, interval=None, limit=None, aggregate=3):
    interval_string = 'histominute' if interval == 'minute' else 'histohour' if interval == 'hour' else 'histoday'
    base = "https://min-api.cryptocompare.com/data/{}?fsym={}&tsym=USD&limit={}&aggregate={}&e=CCCAGG"
    string = base.format(interval_string, coin.upper(), limit, aggregate)
    response = requests.get(string).json()
    return response

