import pyttsx3
from PyPDF2 import PdfReader
import threading
import keyboard  # Import the keyboard library

pdf = None
stop_thread = False  # Variable to signal stopping the playback


def play(pdfReader):
    global pdf
    global stop_thread

    speaker = pyttsx3.init()

    for page_num in range(len(pdfReader.pages)):
        if stop_thread:
            break  # Exit the loop if stop_thread is True
        text = pdfReader.pages[page_num].extract_text()
        speaker.say(text)
        speaker.runAndWait()

    speaker.stop()


def stop_playback():
    global stop_thread
    input("Press Enter to stop playback...")
    stop_thread = True  # Set the flag to stop playback


file = input("Enter your PDF file name: ")

while True:
    try:
        pdf = PdfReader(file)
        break
    except Exception as e:
        print("An error occurred:\n", e)
        print("\nEnter the file name again:\n")
        file = input("Enter your PDF file name: ")

# Create a separate thread for playback
playback_thread = threading.Thread(target=play, args=(pdf,))
playback_thread.start()

# Start a thread for stopping playback with keyboard input
keyboard.add_hotkey("q", lambda: stop_playback())
keyboard.wait()  # Wait for the hotkey event

# Wait for the playback to finish
playback_thread.join()
