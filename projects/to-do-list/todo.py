class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "status": "Not Started"})
        print("Task added: ", task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                status = task["status"]
                task_text = task["task"]

                color_code = {
                    "Not Started": "\033[37m",  # Light Gray
                    "In Progress": "\033[34m",  # Blue
                    "Done": "\033[32m",  # Green
                }
                color_reset = "\033[0m"

                print(f"{i}. {color_code[status]}{task_text}{color_reset} - {status}")

    def update_task_status(self, task_index, new_status):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["status"] = new_status
            print(f"Updated task status: {self.tasks[task_index - 1]['task']} is now {new_status}")
        else:
            print("Invalid task index")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Removed task: {removed_task['task']}")
        else:
            print("Invalid task index")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as In Progress")
        print("4. Mark Task as Done")
        print("5. Remove Task")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == "2":
            to_do_list.view_tasks()
        elif choice == "3":
            to_do_list.view_tasks()
            index = int(input("Enter the task number to mark as In Progress: "))
            to_do_list.update_task_status(index, "In Progress")
        elif choice == "4":
            to_do_list.view_tasks()
            index = int(input("Enter the task number to mark as Done: "))
            to_do_list.update_task_status(index, "Done")
        elif choice == "5":
            to_do_list.view_tasks()
            index = int(input("Enter the task number to remove: "))
            to_do_list.remove_task(index)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
