# Importing all the necessary modules
from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer  # pip install pygame
import os

# Initializing the root window and pygame.mixer

# Initializing the mixer
mixer.init()

# Creating the master GUI for python music player
root = Tk()
root.geometry("700x220")
root.title("Sangeet")
root.resizable(0, 0)


# Play, Stop, Load and Pause & Resume functions
def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))

    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()

    status.set("Song PLAYING")


def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Song STOPPED")


def load(listbox):
    os.chdir(filedialog.askdirectory(title="Select Folder"))

    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)


def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Song PAUSED")


def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Song RESUMED")


# All the frames
song_frame = LabelFrame(
    root, text="Current Song", bg="MediumPurple1", width=400, height=80
)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(
    root, text="Control Buttons", bg="purple3", width=400, height=120
)
button_frame.place(y=80)

listbox_frame = LabelFrame(root, text="Playlist", bg="purple4")
listbox_frame.place(x=400, y=0, height=200, width=300)

# All StringVar variables
current_song = StringVar(root, value="Not selected")

song_status = StringVar(root, value="Not Available")


# Playlist ListBox
playlist = Listbox(listbox_frame, font=("Helvetica", 11), selectbackground="snow3")

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playlist.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playlist.yview)

playlist.pack(fill=BOTH, padx=5, pady=5)


# SongFrame Labels
Label(
    song_frame, text="CURRENTLY PLAYING:", bg="snow3", font=("Times", 10, "bold")
).place(x=5, y=20)

song_lbl = Label(
    song_frame, textvariable=current_song, bg="snow3", font=("Times", 12), width=25
)
song_lbl.place(x=150, y=20)


# Buttons in the main screen
pause_btn = Button(
    button_frame,
    text="Pause",
    bg="snow3",
    font=("Georgia", 13),
    width=7,
    command=lambda: pause_song(song_status),
)
pause_btn.place(x=15, y=10)

stop_btn = Button(
    button_frame,
    text="Stop",
    bg="snow3",
    font=("Georgia", 13),
    width=7,
    command=lambda: stop_song(song_status),
)
stop_btn.place(x=105, y=10)

play_btn = Button(
    button_frame,
    text="Play",
    bg="snow3",
    font=("Georgia", 13),
    width=7,
    command=lambda: play_song(current_song, playlist, song_status),
)
play_btn.place(x=195, y=10)

resume_btn = Button(
    button_frame,
    text="Resume",
    bg="snow3",
    font=("Georgia", 13),
    width=7,
    command=lambda: resume_song(song_status),
)
resume_btn.place(x=285, y=10)

load_btn = Button(
    button_frame,
    text="Load Directory",
    bg="snow3",
    font=("Georgia", 13),
    width=35,
    command=lambda: load(playlist),
)
load_btn.place(x=10, y=55)

# Label at the bottom that displays the state of the music
Label(root, textvariable=song_status, bg="snow", font=("Times", 9), justify=LEFT).pack(
    side=BOTTOM, fill=X
)


# Finalizing the GUI
root.update()
root.mainloop()
