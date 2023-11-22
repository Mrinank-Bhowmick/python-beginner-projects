import tkinter as tk
from tkinter import simpledialog
from datetime import datetime
from tkcalendar import Calendar
import pickle

# Define an empty list to store tasks
tasks = []

# Priority colors
priority_colors = {
    "High": "red",
    "Medium": "orange",
    "Low": "green",
}

# Load tasks from a file (if it exists)
def load_tasks():
    try:
        with open("tasks.pkl", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

tasks = load_tasks()

# Create a function to load and display tasks
def display_tasks():
    for task_info in tasks:
        task = task_info["task"]
        priority = task_info["priority"]
        due_date = task_info["due_date"]
        task_text = f"{len(task_list.get(0, 'end')) + 1}. {task} (Priority: {priority}, Due Date: {due_date})"
        task_list.insert("end", task_text)
        task_list.itemconfig("end", {'fg': priority_colors.get(priority, 'black')})

# Adding Task
def add_task():
    task = task_entry.get()
    priority = task_priority.get()
    due_date = task_due_date.get()
    
    if task:
        task_info = {
            "task": task,
            "priority": priority,
            "due_date": due_date
        }
        tasks.append(task_info)
        task_entry.delete(0, "end")  # Clear the entry field
        update_task_list()
        status_label.config(text="Task added: " + task, fg="green")
        save_tasks_to_file()

# Removing Task
def remove_selected_task():
    selected_task = task_list.curselection()
    if selected_task:
        index = selected_task[0]
        task_info = tasks[index]
        tasks.pop(index)
        update_task_list()
        status_label.config(text="Task removed: " + task_info['task'], fg="red")
        save_tasks_to_file()
    else:
        status_label.config(text="No task selected.", fg="red")

# Save tasks to a file
def save_tasks_to_file():
    with open("tasks.pkl", "wb") as file:
        pickle.dump(tasks, file)

# Show the calendar for selecting due date
def show_calendar():
    date_str = task_due_date.get()
    if date_str:
        selected_date = datetime.strptime(date_str, "%Y-%m-%d")
    else:
        selected_date = datetime.now()
    
    new_date = simpledialog.askstring("Select Due Date", "Enter a date (YYYY-MM-DD):", parent=root, initialvalue=selected_date.strftime("%Y-%m-%d"))
    
    if new_date:
        task_due_date.delete(0, "end")
        task_due_date.insert(0, new_date)

# Update the task list in the UI with priority-based colors
def update_task_list():
    task_list.delete(0, "end")
    for index, task_info in enumerate(tasks, start=1):
        task = task_info["task"]
        priority = task_info["priority"]
        due_date = task_info["due_date"]
        task_text = f"{index}. {task} (Priority: {priority}, Due Date: {due_date})"
        task_list.insert("end", task_text)
        task_list.itemconfig(index, {'fg': priority_colors.get(priority, 'black')})

# Create the main window
root = tk.Tk()
root.title("Interactive To-Do List with Priority and Due Date")

# Create an entry field for tasks
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Create a priority dropdown
priority_options = ["High", "Medium", "Low"]
task_priority = tk.StringVar()
task_priority.set(priority_options[0])  # Set default value
priority_label = tk.Label(root, text="Priority:")
priority_label.pack()
priority_menu = tk.OptionMenu(root, task_priority, *priority_options)
priority_menu.pack()

# Create a due date entry with a calendar button
due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
due_date_label.pack()
due_date_frame = tk.Frame(root)
due_date_frame.pack()
task_due_date = tk.Entry(due_date_frame, width=10)
task_due_date.pack(side="left")
calendar_button = tk.Button(due_date_frame, text="Calendar", command=show_calendar)
calendar_button.pack(side="left")

# Create buttons for Add, Remove, and Quit
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_selected_task)
quit_button = tk.Button(root, text="Quit", command=root.quit)

add_button.pack()
remove_button.pack()
quit_button.pack()

# Create a listbox to display tasks
task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=60)
task_list.pack()

# Create a status label for feedback
status_label = tk.Label(root, text="", fg="black")
status_label.pack()

# Load and display tasks
display_tasks()

# Run the application
root.mainloop()
