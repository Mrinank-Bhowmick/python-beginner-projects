# before running this code, install the following package:pip install ttkthemes

import random
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedStyle


# Function to generate a random story
def generate_story():
    when = [
        "A few years ago",
        "Yesterday",
        "Last night",
        "A long time ago",
        "On 20th Jan",
    ]
    who = ["a rabbit", "an elephant", "a mouse", "a turtle", "a cat"]
    name = ["Ali", "Miriam", "Daniel", "Hoouk", "Starwalker"]
    residence = ["Barcelona", "India", "Germany", "Venice", "England"]
    went = ["cinema", "university", "seminar", "school", "laundry"]
    happened = [
        "made a lot of friends",
        "ate a delicious meal",
        "discovered a hidden treasure",
        "solved a mystery",
        "wrote a best-selling novel",
    ]

    story = []
    total_words = 0

    while total_words < 100:
        sentence = (
            random.choice(when)
            + ", "
            + random.choice(who)
            + " named "
            + random.choice(name)
            + ", who lived in "
            + random.choice(residence)
            + ", decided to go to the "
            + random.choice(went)
            + ". "
            + random.choice(name)
            + " "
            + random.choice(happened)
            + " while at the "
            + random.choice(went)
            + "."
        )

        story.append(sentence)
        total_words += len(sentence.split())

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "\n".join(story))
    result_text.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("Python Story Generator")

# Use a themed style for improved aesthetics
style = ThemedStyle(root)
style.set_theme("arc")  # You can choose from various themes provided by ttkthemes

# Create a custom style with a blue gradient background for the button
custom_style = ttk.Style()
custom_style.configure(
    "BlueGradient.TButton",
    background="#007acc",  # Start color of the gradient
    foreground="Black",  # Text color
    borderwidth=0,  # Remove the default border
    focuscolor="#007acc",
)  # Color when the button is clicked

# Create a button with the custom style
generate_button = ttk.Button(
    root, text="Generate Story", style="BlueGradient.TButton", command=generate_story
)
generate_button.pack(pady=10, ipadx=10, ipady=5)

# Create a scrolled text widget with rounded corners to display the generated story
result_text = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, height=10, width=40, state=tk.DISABLED
)
result_text.pack(padx=20, pady=10)

# Start the GUI main loop
root.mainloop()
