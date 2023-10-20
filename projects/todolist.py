# Initialize an empty list to store tasks
import pickle
import os

# File to store tasks data
tasks_file = "tasks.pkl"

# Function to load tasks from local storage
def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, "rb") as file:
            return pickle.load(file)
    else:
        return []

# Function to save tasks to local storage
def save_tasks():
    with open(tasks_file, "wb") as file:
        pickle.dump(tasks, file)

# Initialize tasks by loading from local storage
tasks = load_tasks()



tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added!")

# Function to display all tasks
def show_tasks():
    print("\nTasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

# Function to mark a task as completed
def complete_task(index):
    if 0 <= index < len(tasks):
        print(f"Task '{tasks[index]}' marked as completed!")
        tasks.pop(index)
    else:
        print("Invalid task index!")

# Function to remove a task
def remove_task(index):
    if 0 <= index < len(tasks):
        print(f"Task '{tasks[index]}' removed!")
        tasks.pop(index)
    else:
        print("Invalid task index!")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        index = int(input("Enter the task number to mark as completed: ")) - 1
        complete_task(index)
    elif choice == "4":
        index = int(input("Enter the task number to remove: ")) - 1
        remove_task(index)
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    save_tasks()

