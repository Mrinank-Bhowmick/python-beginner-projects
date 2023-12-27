from pickle import dump, load


def add_task(tasks):
    if tasks is not None:
        new_tasks = [task.strip() for task in tasks.split(',')]
        todo_list.extend(new_tasks)
        print("Task(s) added!")
    else:
        print("No task specified to add.")


def remove_task(task_nums):
    global todo_list
    updated_list = [task for index, task in enumerate(todo_list) if index not in task_nums]
    todo_list = updated_list
    print("Task(s) removed!")
    return updated_list


def remove_task_by_value(value):
    global todo_list
    updated_list = [task for task in todo_list if task not in value]
    todo_list = updated_list  # Update the global variable
    print("Task(s) removed!")
    return updated_list


def display_tasks():
    if not todo_list:
        print("No tasks to display.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")


def get_user_input():
    user_input = input("Type a number and tasks (comma-separated):"
                       " 1. Add tasks, 2. Remove tasks, 3. Display tasks, 4. Quit: ")
    parts = user_input.split(',', 1)
    choice = parts[0].strip()
    if len(parts) > 1:
        tasks = parts[1].strip()
        print(tasks)
    else:
        tasks = None
    return choice, tasks


def process_user_input(choice, tasks):
    global todo_list
    # Convert choice to integer
    choice = int(choice)

    if choice == 1:
        add_task(tasks)
    elif choice == 2:
        if not todo_list:
            print("No tasks to remove.")
        elif tasks is not None:
            if tasks and all(num.strip().isdigit() for num in tasks.split(',')):
                task_nums = [int(num.strip()) - 1 for num in tasks.split(',')]
                print(task_nums)
                todo_list = remove_task(task_nums)
            else:
                tasks_list = [task.strip() for task in tasks.split(',')]
                print(tasks_list)
                todo_list = remove_task_by_value(tasks_list)
        else:
            print("No task specified to remove.")
    elif choice == 3:
        display_tasks()
    elif choice == 4:
        with open("todo.pickle", "wb") as file_out:
            dump(todo_list, file_out)
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Try again.")


if __name__ == "__main__":
    try:
        with open("todo.pickle", "rb+") as file_in:
            todo_list = load(file_in)
    except FileNotFoundError:
        todo_list = []

    print("Welcome to ToDo List!")

    while True:
        user_choice, user_tasks = get_user_input()
        process_user_input(user_choice, user_tasks)
