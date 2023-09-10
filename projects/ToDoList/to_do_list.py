from pickle import dump, load


def add_task(task):
    todo_list.append(task)
    print("Task added!")


def remove_task(task_num):
    if 0 <= task_num < len(todo_list):
        del todo_list[task_num]
        print("Task removed!")
    else:
        print("Invalid task number!")


def display_tasks():
    if not todo_list:  # If list is empty
        print("No tasks to display.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")


def get_choice():
    while True:
        try:
            choice = int(
                input(
                    "Type a number: 1. Adding a task, 2. Removing a task, 3. Displaying tasks, 4. Quit: "
                )
            )
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 4.")


if __name__ == "__main__":
    # Loading the pickle file into python as a list
    try:
        with open("todo.pickle", "rb+") as file_in:
            todo_list = load(file_in)
    except FileNotFoundError:
        todo_list = []

    print("Welcome to ToDo List!")

    while True:
        user_choice = get_choice()

        # Adding a task
        if user_choice == 1:
            new_task = input("Type a new task: ")
            add_task(new_task)

        # Removing a task
        elif user_choice == 2:
            if not todo_list:  # If list is empty
                print("No tasks to remove.")
            else:
                task_num = int(input("Enter the task number to delete: ")) - 1
                remove_task(task_num)

        # Displaying tasks
        elif user_choice == 3:
            display_tasks()

        # Quit
        elif user_choice == 4:
            # Dumping the list into a pickle file
            with open("todo.pickle", "wb") as file_out:
                dump(todo_list, file_out)
            print("Goodbye!")
            break


#####################################

# CODE CONTRIBUTED BY: Ota Hina
# Dynamic funcionality added by : komsenapati

#####################################
