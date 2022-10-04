from tkinter import *
from tkinter import messagebox
import pyqrcode

ws = Tk()
ws.title("QRCODE GENERATOR")
ws.config(bg='#FFFFF0')


def generate_QR():
    if len(user_input.get()) != 0:
        global qr, img
        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data=qr.xbm(scale=12))
    else:
        messagebox.showwarning('warning', 'All Fields are Required!')
    try:
        display_code()
    except:
        pass


def display_code():
    img_lbl.config(image=img)
    output.config(text="QR code of " + user_input.get())


lbl = Label(ws, text="Enter message or URL", bg='#FFFFFF')
lbl.pack()
user_input = StringVar()
entry = Entry(ws, textvariable=user_input)
entry.pack(padx=10)
button = Button(ws, text="Generate QR Code", width=15, command=generate_QR)
button.pack(pady=12)
img_lbl = Label(ws, bg='#FFFFFF')
img_lbl.pack()
output = Label(ws, text="", bg='#FFFFFF')
output.pack()
ws.mainloop()
