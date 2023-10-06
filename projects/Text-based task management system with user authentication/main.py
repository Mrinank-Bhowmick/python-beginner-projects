import sqlite3
import hashlib
conn = sqlite3.connect("task_manager.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        priority INTEGER,
        username TEXT,
        FOREIGN KEY (username) REFERENCES users (username)
    )
""")
conn.commit()

# Function to create a new user account
def create_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("User account created successfully!")

# Function to authenticate a user
def authenticate_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT username FROM users WHERE username=? AND password=?", (username, hashed_password))
    user = cursor.fetchone()
    return user is not None

# Function to add a new task
def add_task(username, title, description, priority):
    cursor.execute("INSERT INTO tasks (title, description, priority, username) VALUES (?, ?, ?, ?)", (title, description, priority, username))
    conn.commit()
    print("Task added successfully!")

# Function to view tasks for a user
def view_tasks(username):
    cursor.execute("SELECT id, title, description, priority FROM tasks WHERE username=?", (username,))
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks found for this user.")
    else:
        print("Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}, Priority: {task[3]}")

# Function to delete a task
def delete_task(username, task_id):
    cursor.execute("DELETE FROM tasks WHERE id=? AND username=?", (task_id, username))
    conn.commit()
    print("Task deleted successfully!")

# Main program loop
while True:
    print("\nTask Manager")
    print("1. Create User Account")
    print("2. Login")
    print("3. Quit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        create_user(username, password)
    elif choice == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if authenticate_user(username, password):
            print(f"Welcome, {username}!")
            while True:
                print("\nTask Options")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Delete Task")
                print("4. Logout")
                
                task_choice = input("Enter your choice: ")
                
                if task_choice == "1":
                    title = input("Enter the task title: ")
                    description = input("Enter the task description: ")
                    priority = int(input("Enter the task priority (1 - High, 2 - Medium, 3 - Low): "))
                    add_task(username, title, description, priority)
                elif task_choice == "2":
                    view_tasks(username)
                elif task_choice == "3":
                    view_tasks(username)
                    task_id = int(input("Enter the task ID to delete: "))
                    delete_task(username, task_id)
                elif task_choice == "4":
                    print("Logged out successfully!")
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Authentication failed. Please try again.")
    elif choice == "3":
        print("Goodbye!")
        conn.close()
        break
    else:
        print("Invalid choice. Please try again.")
