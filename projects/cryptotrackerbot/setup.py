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


import setuptools


setuptools.setup(

    name="cryptotrackerbot",
    version="1",

    license="AGPL-3.0",

    author="Dario 91DarioDev",
    author_email="dariomsn@hotmail.it",

    install_requires=[
        "python-telegram-bot",
        "requests",
        "matplotlib<2.2.0",
        "image"
    ],

    packages=[
        "cryptotrackerbot",
    ],

    entry_points={
        "console_scripts": [
            "cryptotrackerbot = cryptotrackerbot.__main__:main",
        ],
    },

    include_package_data=True,
    zip_safe=False,

    classifiers=[
        "Not on PyPI"
    ],

)
