import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

# Database initialization
conn = sqlite3.connect("budget.db")
c = conn.cursor()
c.execute(
    """CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL
            )"""
)
conn.commit()


# Function to add a transaction to the database.
def add_transaction():
    """
    Adds a transaction to the database based on user input.
    """
    date = date_entry.get()
    description = description_entry.get()
    amount = amount_entry.get()
    category = category_combobox.get()

    if date and description and amount and category:
        c.execute(
            "INSERT INTO transactions (date, description, amount, category) VALUES (?, ?, ?, ?)",
            (date, description, amount, category),
        )
        conn.commit()
        clear_entries()
        messagebox.showinfo("Success", "Transaction added successfully!")
        update_transaction_list()
        update_balance()
    else:
        messagebox.showwarning("Warning", "Please fill in all fields.")


def delete_transaction():
    """
    Deletes a selected transaction from the database.
    """
    selected_index = transaction_listbox.curselection()
    if selected_index:
        transaction_id = transaction_listbox.get(selected_index)[0]
        c.execute("DELETE FROM transactions WHERE id=?", (transaction_id,))
        conn.commit()
        update_transaction_list()
        update_balance()
        messagebox.showinfo("Success", "Transaction deleted successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a transaction to delete")


# Function to clear input fields.


def clear_entries():
    """
    Clears all input fields.
    """
    date_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_combobox.set("")
    category_combobox.config(state="readonly")


# Function to update the transaction list.
def update_transaction_list():
    """
    Updates the displayed transaction list based on the database entries.
    """
    transaction_listbox.delete(0, tk.END)
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()
    for transaction in transactions:
        transaction_listbox.insert(tk.END, transaction)


# Function to calculate and display the current balance.
def update_balance():
    """
    Calculates and displays the current balance based on income and expenses.
    """
    c.execute("SELECT SUM(amount) FROM transactions")
    total_income = c.fetchone()[0]
    if total_income is None:
        total_income = 0.0
    c.execute("SELECT SUM(amount) FROM transactions WHERE amount < 0")
    total_expense = c.fetchone()[0]
    if total_expense is None:
        total_expense = 0.0
    balance = total_income - total_expense
    balance_label.config(text=f"Current Balance: ${balance:.2f}")


# Create the main window.
root = tk.Tk()
root.title("Personal Budget Manager")
root.columnconfigure(1, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(5, weight=1)

# Create and configure widgets.
delete_button = tk.Button(root, text="Delete Transaction", command=delete_transaction)
date_label = tk.Label(root, text="Date:")
date_entry = tk.Entry(root, width=15)
description_label = tk.Label(root, text="Description:")
description_entry = tk.Entry(root, width=30)
amount_label = tk.Label(root, text="Amount ($):")
amount_entry = tk.Entry(root, width=15)
category_label = tk.Label(root, text="Category:")
category_combobox = ttk.Combobox(
    root,
    values=[
        "Income",
        "Housing",
        "Food",
        "Transportation",
        "Utilities",
        "Entertainment",
        "Health",
        "Other",
    ],
)
add_button = tk.Button(root, text="Add Transaction", command=add_transaction)
transaction_listbox = tk.Listbox(root, width=50)
balance_label = tk.Label(root, text="Current Balance: $0.00")

# Place widgets in the window.
delete_button.grid(row=0, column=9, padx=10, pady=10)
date_label.grid(row=0, column=0, padx=10, pady=10)
date_entry.grid(row=0, column=1, padx=10, pady=10)
description_label.grid(row=0, column=2, padx=10, pady=10)
description_entry.grid(row=0, column=3, padx=10, pady=10)
amount_label.grid(row=0, column=4, padx=10, pady=10)
amount_entry.grid(row=0, column=5, padx=10, pady=10)
category_label.grid(row=0, column=6, padx=10, pady=10)
category_combobox.grid(row=0, column=7, padx=10, pady=10)
add_button.grid(row=0, column=8, padx=10, pady=10)
transaction_listbox.grid(row=1, column=0, columnspan=9, padx=10, pady=10)
balance_label.grid(row=2, column=0, columnspan=9, padx=10, pady=10)

# Initialize the transaction list and balance.
update_transaction_list()
update_balance()

root.mainloop()
