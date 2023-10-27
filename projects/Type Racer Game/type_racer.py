import tkinter as tk
from tkinter import ttk
import random
import time

# List of random English sentences for the game
sentences = [
    "The quick brown fox jumps over the lazy dog",
    "Python is an interpreted high-level programming language",
    "I'm learning to code with Python and it's fun",
    "A journey of a thousand miles begins with a single step",
    "Coding is not just about algorithms, it's about logic",
    "Practice makes perfect in programming",
    "Innovation distinguishes between a leader and a follower",
    "The only way to do great work is to love what you do",
    "Coding is the language of the future",
    "Keep calm and code on",
]

# Initialize the game
score = 0
start_time = 0
current_sentence = random.choice(sentences)
timer_duration = 30  # Countdown timer duration in seconds
countdown_duration = 5  # Countdown timer duration in seconds

# Flag to indicate whether the game has started
game_started = False


# Function to start the game with a countdown
def start_game():
    global start_time, current_sentence, timer_duration, score, game_started
    score = 0
    timer_duration = 30  # Reset the timer duration to 30 seconds
    countdown_label.config(text="Get ready!")
    root.update()
    time.sleep(1)
    for i in range(countdown_duration, 0, -1):  # Use countdown duration
        countdown_label.config(text=str(i))
        root.update()
        time.sleep(1)
    countdown_label.config(text="Go!")
    root.update()
    time.sleep(1)
    countdown_label.config(text="")
    root.update()
    start_time = time.time()
    current_sentence = random.choice(sentences)  # Select a new random sentence
    sentence_label.config(text=current_sentence)
    input_box.delete(0, tk.END)
    input_box.focus()
    input_box.config(
        foreground="black", width=40
    )  # Reset text color and increase width
    game_started = True  # Set the game started flag
    start_main_timer()  # Start the main game timer after the countdown


# Function to reset the game
def reset_game():
    global game_started
    game_started = False
    countdown_label.config(text="")
    submit_score()  # Submit the score to reset the progress bar


# Function to start the main game timer
def start_main_timer():
    global timer_duration, game_started
    if timer_duration > 0 and game_started:
        timer_label.config(text=f"Time left: {timer_duration} seconds")
        countdown_label.config(text=str(timer_duration))  # Update countdown_label here
        timer_duration -= 1
        root.after(1000, start_main_timer)
    elif game_started:
        timer_label.config(text="Time's up!")
        submit_score()


# Function to handle typing and change text color
def check_input(event):
    input_text = input_box.get()
    if current_sentence.startswith(input_text):
        input_box.config(foreground="green")  # Correct text color
        update_progress_bar(len(input_text))
    else:
        input_box.config(foreground="red")  # Incorrect text color


# Function to handle submission of score
def submit_score():
    global current_sentence, game_started
    end_time = time.time()
    time_taken = round(end_time - start_time, 2)
    if input_box.get() == current_sentence:
        wpm = calculate_wpm(time_taken, len(current_sentence.split()))
        result_label.config(
            text=f"Correct! Time taken: {time_taken} seconds, WPM: {wpm}",
            foreground="green",
        )
        reset_progress_bar()
        animate_result_label()
        current_sentence = random.choice(sentences)  # Select a new random sentence
        start_game()
    else:
        result_label.config(
            text=f"Incorrect. Time taken: {time_taken} seconds", foreground="red"
        )
        animate_result_label()


# Function to animate the result label
def animate_result_label():
    result_label.config(foreground="red")
    root.after(100, lambda: result_label.config(foreground="black"))
    root.after(200, lambda: result_label.config(foreground="red"))
    root.after(300, lambda: result_label.config(foreground="black"))
    root.after(400, lambda: result_label.config(foreground="red"))
    root.after(500, lambda: result_label.config(foreground="black"))
    root.after(600, lambda: result_label.config(foreground="red"))
    root.after(700, lambda: result_label.config(foreground="black"))
    root.after(800, lambda: result_label.config(foreground="red"))
    root.after(900, lambda: result_label.config(foreground="black"))
    root.after(1000, lambda: result_label.config(foreground="red"))
    root.after(1100, lambda: result_label.config(text="", foreground="black"))


# Function to update the progress bar
def update_progress_bar(length):
    progress = min(length / len(current_sentence), 1.0) * 100
    progressbar_label.config(text=f"Progress: {int(progress)}%")
    progressbar["value"] = progress


# Function to reset the progress bar
def reset_progress_bar():
    progressbar_label.config(text="Progress: 0%")
    progressbar["value"] = 0


# Countdown timer function
def countdown():
    global timer_duration, game_started
    if timer_duration > 0 and game_started:
        timer_label.config(text=f"Time left: {timer_duration} seconds")
        countdown_label.config(text=str(timer_duration))  # Update countdown_label here
        timer_duration -= 1
        root.after(1000, countdown)


# Function to calculate WPM
def calculate_wpm(time_taken, word_count):
    minutes = time_taken / 60
    wpm = (word_count / 5) / minutes
    return round(wpm)


# Initialize the GUI
root = tk.Tk()
root.geometry("800x400")
root.title("TypeRacer")


# Create the widgets with ttk themes
style = ttk.Style()
style.configure("TLabel", foreground="black", font=("Arial", 14))
style.configure("TButton", font=("Arial", 16))

sentence_label = ttk.Label(root, text=current_sentence, wraplength=700, justify="left")
input_box = ttk.Entry(root, font=("Arial", 16), width=40)  # Increase width
submit_button = ttk.Button(root, text="Submit", command=submit_score)
reset_button = ttk.Button(root, text="Reset", command=reset_game)
result_label = ttk.Label(root)
progressbar_label = ttk.Label(root, text="Progress: 0%")
progressbar = ttk.Progressbar(
    root, orient=tk.HORIZONTAL, length=200, mode="determinate"
)
timer_label = ttk.Label(root, text=f"Time left: {timer_duration} seconds")
countdown_label = ttk.Label(root, font=("Arial", 24), foreground="red")

# Add the widgets to the GUI
sentence_label.pack(pady=20)
input_box.pack(pady=10)
submit_button.pack(side=tk.RIGHT, padx=10)
reset_button.pack(side=tk.RIGHT, padx=10)
result_label.pack(pady=10)
progressbar_label.pack(pady=10)
progressbar.pack(pady=10)
timer_label.pack(pady=10)
countdown_label.pack(pady=10)

# Bind the typing event to the input_box
input_box.bind("<KeyRelease>", check_input)

# Start the game
start_game()

# Start the GUI event loop
root.mainloop()
