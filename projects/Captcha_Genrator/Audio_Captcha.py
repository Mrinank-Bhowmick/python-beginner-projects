from io import BytesIO
from tkinter import *
from tkinter import messagebox
import pygame
from random import *
from captcha.audio import AudioCaptcha

audio = AudioCaptcha()
pygame.mixer.init()
captcha_text = ""


def create_audio_captcha():
    global captcha_text
    captcha_text = str(randint(1000, 9999))
    print(captcha_text)
    audio.write(captcha_text, "audio" + ".wav")


create_audio_captcha()

root = Tk()
root.title("Audio Captcha")


def play_audio():
    pygame.mixer.music.load("audio" + ".wav")
    pygame.mixer.music.play()


def verify_audio():
    text = check.get("1.0", "end-1c")
    global captcha_text
    if text == captcha_text:
        messagebox.showinfo("SUCCESS", "Verified")
    else:
        messagebox.showinfo("ALERT", "Not Verified")


heading_label = Label(root, text="Enter the Audio Captcha", height=2, width=50)
check = Text(root, height=2, width=50)
play_button = Button(root, text="Play Audio", command=play_audio)
submit = Button(root, text="Submit", command=verify_audio)
renew = Button(root, text="Renew", command=create_audio_captcha)

heading_label.pack()
check.pack()
play_button.pack(side=LEFT, padx=35, pady=5)
renew.pack(side=LEFT, padx=40, pady=5)
submit.pack(side=RIGHT, padx=35, pady=5)

root.mainloop()
