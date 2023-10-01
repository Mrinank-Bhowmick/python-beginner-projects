import tkinter as tk
from tkinter import messagebox
import random
import sys  # Import the sys module for exiting the application

# Define upper and lower bounds for the game
lower_limit = 1
upper_limit = 10
secret_number = random.randint(lower_limit, upper_limit)


# Function to check if the user's guess is correct
def check_guess():
    user_guess = int(guess_entry.get())
    if user_guess == secret_number:
        messagebox.showinfo("Congratulations", "Congratulations! You guessed it!")
    elif user_guess < secret_number:
        result_label.config(text="Try a higher number.")
    else:
        result_label.config(text="Try a lower number.")


# Function to exit the application
def exit_game():
    root.destroy()  # Close the Tkinter window and exit the application


# Create the main application window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x200")

# Change the background color of the window and label to salmon
root.configure(bg="pink1")

# Create and place widgets using grid
instructions_label = tk.Label(
    root, text=f"Guess a number between {lower_limit} and {upper_limit}:", bg="pink1"
)
instructions_label.grid(row=0, column=0, columnspan=2)

guess_entry = tk.Entry(root)
guess_entry.grid(row=1, column=0, columnspan=2)

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.grid(row=2, column=0)

exit_button = tk.Button(root, text="Exit", command=exit_game)
exit_button.grid(row=2, column=1)

result_label = tk.Label(root, text="", bg="pink1")
result_label.grid(row=3, column=0, columnspan=2)

# Center-align the widgets
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run the main loop
root.mainloop()
