import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def list_tasks(tasks):
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks found.")

def add_task(tasks, new_task):
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added.")

def update_task(tasks, task_index, updated_task):
    if 0 <= task_index < len(tasks):
        tasks[task_index] = updated_task
        save_tasks(tasks)
        print("Task updated.")
    else:
        print("Invalid task index.")

def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Deleted task: {deleted_task}")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. List tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter a new task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            task_index = int(input("Enter the task index to update: ")) - 1
            updated_task = input("Enter the updated task: ")
            update_task(tasks, task_index, updated_task)
        elif choice == "4":
            task_index = int(input("Enter the task index to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
