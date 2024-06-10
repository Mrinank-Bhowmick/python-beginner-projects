# Py Text Sender

[![License](https://img.shields.io/static/v1?label=License&message=GPL-3-0&color=blue&?style=plastic&logo=appveyor)](https://opensource.org/license/GPL-3-0)



## Table Of Content

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [GitHub](#github)
- [License](#license)




![GitHub repo size](https://img.shields.io/github/repo-size/robertlent/py_auto_textmessage?style=plastic)

  ![GitHub top language](https://img.shields.io/github/languages/top/robertlent/py_auto_textmessage?style=plastic)



## Description

  Python script to send a text message through textbelt. A message can also be scheduled to go out every day at a certain time.

Using the program with the included key 'textbelt', the user can send one free text message per day.



## Installation

1. Download main.py and requirements.txt to your machine.
2. Change to the directory that the files were downloaded to, create a virtual environment, and activate it using `cd [/path/to/files] && python3 -m venv venv && source venv/bin/activate`
3. Install dependencies using `pip3 install -r requirements.txt`



Py Text Sender is built with the following tools and libraries: <ul><li>Python</li><li><a href='https://textbelt.com/'>textbelt</a></li></ul>



## Usage

1. Run the program with `python3 main.py`
2. Follow the prompts:
    - Choose to either send a one-time text message or schedule a text message every day at a specific time.
    - Provide the phone number you would like to send the text to.
    - Your default command-line editor will open, prompting you for the text's message.
    - If you chose option 1, the number and message will be sent to the textbelt api and a 'success' or 'failure' response will be received.
    - If you chose option 2, you will be prompted to enter the time of day that you want to schedule the text to be sent.
        - The program will continue running, sending your message every day at the provided time, until you kill it.


## GitHub

<a href="https://github.com/robertlent"><strong>robertlent</a></strong>



## License

[![License](https://img.shields.io/static/v1?label=License&message=GPL-3-0&color=blue&?style=plastic&logo=appveyor)](https://opensource.org/license/GPL-3-0)
