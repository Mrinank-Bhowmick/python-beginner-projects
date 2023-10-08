import os
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Initialize pygame
pygame.init()

# Function to list video files in a directory
def list_video_files(directory):
    video_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".mp4", ".avi", ".mkv")):
                video_files.append(os.path.join(root, file))
    return video_files

# Function to play video
def play_video():
    selected_item = video_listbox.curselection()
    if selected_item:
        index = int(selected_item[0])
        video = pygame.movie.Movie(video_files[index])
        video.set_display(video_display)
        video.play()

# Function to pause video
def pause_video():
    pygame.mixer.music.pause()

# Function to resume video
def resume_video():
    pygame.mixer.music.unpause()

# Function to stop video
def stop_video():
    pygame.mixer.music.stop()

# Function to open a directory dialog and set the video directory
def choose_directory():
    global video_directory
    video_directory = filedialog.askdirectory()
    video_files = list_video_files(video_directory)
    video_listbox.delete(0, tk.END)
    for file in video_files:
        video_listbox.insert(tk.END, os.path.basename(file))

# Create a tkinter window
root = tk.Tk()
# Adjust size
root.geometry("420x300")
 
# set minimum window size value
root.minsize(420, 300)
 
# set maximum window size value
root.maxsize(420, 300)
root.title("Video Player")

# Create and configure a frame for buttons
button_frame = ttk.Frame(root)
button_frame.grid(row=1, column=0, padx=20, pady=10)

# Create buttons
play_button = ttk.Button(button_frame, text="Play", command=play_video)
pause_button = ttk.Button(button_frame, text="Pause", command=pause_video)
resume_button = ttk.Button(button_frame, text="Resume", command=resume_video)
stop_button = ttk.Button(button_frame, text="Stop", command=stop_video)

# Grid layout for buttons
play_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0, column=1, padx=10)
resume_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=3, padx=10)

# Create a frame for the video list
list_frame = ttk.Frame(root)
list_frame.grid(row=0, column=0, padx=20, pady=10)

# Create a listbox to display video files
video_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, width=50)
video_listbox.pack()

# Create a button to choose the video directory
choose_button = ttk.Button(list_frame, text="Choose Video Directory", command=choose_directory)
choose_button.pack()

# Initialize the video directory
video_directory = ""

# Create a Pygame display for video playback
video_display = pygame.display.set_mode((640, 480))

# Run the tkinter main loop
root.mainloop()
