import tkinter
from time import strftime

top = tkinter.Tk()
top.title("Clock")
top.resizable(0, 0)


def time():
    string = strftime("%H:%M:%S %p")
    clockTime.config(text=string)
    clockTime.after(1000, time)


clockTime = tkinter.Label(
    top,
    font=(
        "courier new",
        40,
    ),
    background="black",
    foreground="white",
)
clockTime.pack(anchor="center")
time()
top.mainloop()
