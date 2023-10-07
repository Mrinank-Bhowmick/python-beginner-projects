import tkinter as tk
from tkinter import messagebox

# Function to add a book to the list
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    
    if title and author:
        book_list.insert(tk.END, f"{title} by {author}")
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter both title and author.")

# Function to remove a selected book from the list
def remove_book():
    try:
        selected_index = book_list.curselection()[0]
        book_list.delete(selected_index)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("Book Organizer")

# Setting Size of app
root.geometry("300x300")

# Create and pack widgets
title_label = tk.Label(root, text="Title:")
title_label.pack()

title_entry = tk.Entry(root)
title_entry.pack()

author_label = tk.Label(root, text="Author:")
author_label.pack()

author_entry = tk.Entry(root)
author_entry.pack()

add_button = tk.Button(root, text="Add Book", command=add_book)
add_button.pack()

remove_button = tk.Button(root, text="Remove Book", command=remove_book)
remove_button.pack()

book_list = tk.Listbox(root)
book_list.pack()

# Start the Tkinter main loop
root.mainloop()
