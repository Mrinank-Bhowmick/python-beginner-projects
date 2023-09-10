import requests
import tkinter as tk


# Function to fetch and display a random quote
def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        data = response.json()
        quote = data["content"]
        author = data["author"]
        quote_text.set(f'"{quote}" - {author}')
    except requests.exceptions.RequestException as e:
        quote_text.set("Failed to fetch a quote. Check your internet connection.")


# Create the main window
root = tk.Tk()
root.title("Random Quote Generator")

# Create a label to display the quote
quote_text = tk.StringVar()
quote_label = tk.Label(
    root, textvariable=quote_text, wraplength=300, font=("Helvetica", 12)
)
quote_label.pack(pady=20)

# Create a button to get a new quote
new_quote_button = tk.Button(root, text="Get a New Quote", command=get_random_quote)
new_quote_button.pack()

# Fetch and display an initial random quote
get_random_quote()

# Start the GUI main loop
root.mainloop()
