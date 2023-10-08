import os
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Initialize pygame mixer
pygame.mixer.init()

# Function to list music files in a directory
def list_music_files(directory):
    music_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".mp3", ".wav")):
                music_files.append(os.path.join(root, file))
    return music_files

# Function to play music
def play_music():
    selected_item = music_listbox.curselection()
    if selected_item:
        index = int(selected_item[0])
        pygame.mixer.music.load(music_files[index])
        pygame.mixer.music.play()

# Function to pause music
def pause_music():
    pygame.mixer.music.pause()

# Function to resume music
def resume_music():
    pygame.mixer.music.unpause()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Function to open a directory dialog and set the music directory
def choose_directory():
    global music_directory
    music_directory = filedialog.askdirectory()
    music_files = list_music_files(music_directory)
    music_listbox.delete(0, tk.END)
    for file in music_files:
        music_listbox.insert(tk.END, os.path.basename(file))

# Create a tkinter window
root = tk.Tk()
# Adjust size
root.geometry("420x300")
 
# set minimum window size value
root.minsize(420, 300)
 
# set maximum window size value
root.maxsize(420, 300)
root.title("Video Player")
root.title("Music Player")

# Create and configure a frame for buttons
button_frame = ttk.Frame(root)
button_frame.grid(row=1, column=0, padx=20, pady=10)

# Create buttons
play_button = ttk.Button(button_frame, text="Play", command=play_music)
pause_button = ttk.Button(button_frame, text="Pause", command=pause_music)
resume_button = ttk.Button(button_frame, text="Resume", command=resume_music)
stop_button = ttk.Button(button_frame, text="Stop", command=stop_music)

# Grid layout for buttons
play_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0, column=1, padx=10)
resume_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=3, padx=10)

# Create a frame for the music list
list_frame = ttk.Frame(root)
list_frame.grid(row=0, column=0, padx=20, pady=10)

# Create a listbox to display music files
music_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, width=50)
music_listbox.pack()

# Create a button to choose the music directory
choose_button = ttk.Button(list_frame, text="Choose Music Directory", command=choose_directory)
choose_button.pack()

# Initialize the music directory
music_directory = ""

# Run the tkinter main loop
root.mainloop()
