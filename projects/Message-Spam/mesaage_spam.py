import random
import pyautogui as pg
import webbrowser as wb
import time

web_url = "https://web.whatsapp.com"
wb.open(web_url)

time.sleep(10)

messages = ('Hello', 'Hey', 'Good Morning')

for _ in range(10):
    message = random.choice(messages)
    
    pg.write(message)
    pg.press('enter')
    
    time.sleep(random.uniform(1, 3))
