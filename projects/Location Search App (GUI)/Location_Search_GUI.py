import tkinter as tk
import pyperclip as pc
import webbrowser

Height = 700
Width = 600
root = tk.Tk()
root.title("Location Search")
canvas_color = "#FB6223"
frame_color = "#2DE3E9"
inner_frame_color = "#2EE3E9"
button_color = "#B8E82D"
entry_color = "#F2FECE"
font_ = ("Handlee", 16)


def search_function(search_term):
    webbrowser.open("https://google.com/maps/place/" + str(search_term))


canvas = tk.Canvas(root, height=Height, width=Width, bg=canvas_color)
canvas.pack()

frame = tk.Frame(root, bg=frame_color, bd=2)
frame.place(relx=0.075, rely=0.1, relwidth=0.85, relheight=0.75)


entry = tk.Entry(frame, bg=entry_color, font=font_)
entry.place(relx=0.16, rely=0.1, relwidth=0.60, relheight=0.05)

label = tk.Label(frame, bg=canvas_color, text="Enter location to search", font=font_)
label.place(relx=0.20, rely=0.2)


button = tk.Button(
    frame,
    font=font_,
    bg=button_color,
    text="Search",
    command=lambda: search_function(entry.get()),
)
button.place(relx=0.77, rely=0.1, relwidth=0.20, relheight=0.05)

root.mainloop()
