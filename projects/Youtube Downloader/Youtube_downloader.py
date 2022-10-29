import os
from pytube import YouTube, exceptions    # pip install pytube
from time import time
from tkinter import *
from customtkinter import *    # pip install customtkinter

# Initialize all the settings
set_appearance_mode("System") # Setting the appearance mode to follow by the app: "System", "Light" or "Dark"
set_default_color_theme("blue") # Setting the theme of the app to follow
for i in os.listdir(os.getcwd()):
    if i == "youtube_downloads": # If there's already a folder called "youtube_downloads", do not create a new one
        break
else:    
    os.mkdir("youtube_downloads") # If there is no folder called "youtube_downloads", create a new one

# Download video function
def download_video(entry_field):
    try:
        start_time = time()
        download_location = "youtube_downloads/"
        YouTube(entry_field).streams.first().download(download_location)
        end_time = time()

        # Showing the download time in a new window
        popup = CTk()
        popup.title("Download Status")
        popup.resizable(False, False)
        popup.geometry("200x100")
        popup.grid_columnconfigure(0, weight=1)
        popup.grid_rowconfigure((0,1), weight=1)
        msg = StringVar()
        msg.set(f"Download successful!\nTotal time taken: {round(end_time-start_time,3)} seconds")
        label = CTkLabel(popup, text=msg.get())
        label.grid(row=0, column=0)
        button = CTkButton(popup, text="OK", command=popup.destroy)
        button.grid(row=1, column=0)
        popup.mainloop()
    except exceptions.RegexMatchError: # If there's an invalid link or empty link, show an error message
        error = CTk()
        error.title("Error")
        error.resizable(False, False)
        error.geometry("300x100")
        error.grid_rowconfigure((0,1), weight=1)
        error.grid_columnconfigure(0, weight=1)
        error_label = CTkLabel(error, text="Please enter a valid YouTube link")
        error_label.grid(row=0, column=0)
        button = CTkButton(error, text="OK", command=error.destroy)
        button.grid(row=1, column=0)
        error.mainloop()

# Initializing the layout of the app
master = CTk()
master.title("YouTube Downloader")
master.grid_rowconfigure((0,1), weight=1)
master.grid_columnconfigure((0,1), weight=1)
master.geometry("350x150")
master.resizable(False, False)
CTkLabel(master, text="Enter YouTube video URL:").grid(row=0, column=0)
entry = CTkEntry(master)
entry.grid(row=0, column=1)
CTkButton(master, text='Download', command=lambda *args: download_video(entry.get())).grid(row=1, column=0, columnspan=2)
master.mainloop()