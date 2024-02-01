# Import necessary libraries
import random
import pyautogui as pg
import webbrowser as wb
import time

# Define the WhatsApp Web URL
web_url = "https://web.whatsapp.com"

# Open the web browser to the WhatsApp Web URL
wb.open(web_url)

# Wait for 10 seconds to allow the user to log in by scanning the QR code
time.sleep(10)

# List of messages to send
messages = ("Hello", "Hey", "Good Morning")

# Send 10 random messages
for _ in range(10):
    # Choose a random message from the list
    message = random.choice(messages)

    # Type and send the message using PyAutoGUI
    pg.write(message)
    pg.press("enter")

    # Pause for a random duration between 1 to 3 seconds
    time.sleep(random.uniform(1, 3))
