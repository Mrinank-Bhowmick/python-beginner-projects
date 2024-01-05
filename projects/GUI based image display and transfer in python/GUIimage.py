import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import shutil


# Function to open an image using file dialog
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo
        global current_image_path
        current_image_path = file_path


# Function to save the current image to a new location
def save_image():
    if current_image_path:
        destination_path = filedialog.asksaveasfilename(defaultextension=".png")
        if destination_path:
            shutil.copy(current_image_path, destination_path)


# Create the main window
root = tk.Tk()
root.title("Image Viewer and Transfer")

# Create a label for displaying images
label = tk.Label(root)
label.pack()

# Create "Open" and "Save As" buttons
open_button = tk.Button(root, text="Open Image", command=open_image)
save_button = tk.Button(root, text="Save Image", command=save_image)
open_button.pack()
save_button.pack()

current_image_path = None

root.mainloop()
