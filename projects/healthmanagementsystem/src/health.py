import datetime
import os


def get_time():
    '''
    Get the current date and time.
    :return:
        datetime- a datetime object to return the current date and time.
    '''
    return datetime.datetime.now()


def log_entry(person, entry_type):
    '''
    Log an entry for a person in a specified file based on the entry type.

    :param person:
        (str)The name of the person whom the entry is being logged.
    :param entry_type:
        (int)Type of entry.
        1: For exercise related entries.
        2. For food related entries.
    :return:
        None
    Example:
        >>> log_entry("Smith", 1)
        Type :
        Ran 5 miles in the morning.
        Written successfully

    Note:
        - For exercise-related entries, the file name will be "{person}-exe.txt".
        - For food-related entries, the file name will be "{person}-food.txt".
        - Invalid entry types will result in an error message and no logging.
    '''
    if entry_type == 1:
        filename = f"{person}-exe.txt"
    elif entry_type == 2:
        filename = f"{person}-food.txt"
    else:
        print("Invalid entry type.")
        return

    value = input("Type here: \n")
    with open(filename, "a") as file:
        file.write(f"{get_time()}: {value}\n")
    print("Written successfully")


def retrieve_entry(person, entry_type):
    '''
    Retrieve and display entries logged for a person based on the entry type.
    :param person:
        (str)The name of the person whose entries are being retrieved.
    :param entry_type:
        (int)The type of the entry to retrieve.
            1: For exercise related entries.
            2: For food related entries.
    :return:
        None
    Example:
        >>> retrieve_entry("Smith", 1)
        2024-06-06 14:30:00: Ran 5 miles in the morning.
        2024-06-06 15:45:00: Did weight training at the gym.

    Note:
        - For exercise-related entries, the file name will be "{person}-exe.txt".
        - For food-related entries, the file name will be "{person}-food.txt".
        - If no records are found for the specified person and entry type, a message will be displayed.
    '''
    if entry_type == 1:
        filename = f"{person}-exe.txt"
    elif entry_type == 2:
        filename = f"{person}-food.txt"
    else:
        print("Invalid entry type.")
        return

    try:
        with open(filename, "r") as file:
            for line in file:
                print(line, end="")
    except FileNotFoundError:
        print(f"No records found for {person}'s {entry_type}")


def input_person_data(person_number):
    '''
    Prompt the user to input data for a specified person and entry type.
    :param person_number:
        (int)The number of the person whom the data is being inputted.
    :return:
        None
    Example:
        >>> input_person_data(1)
        Enter 1 for exercise and 2 for food: 1
        Type here:
        Ran 5 miles in the morning.
        Written successfully

    Note:
        - The function prompts the user to enter 1 for exercise-related data and 2 for food-related data.
        - Depending on the person number provided,
          the function logs the data for the corresponding person using the log_entry function.
    '''
    entry_type = int(input("Enter 1 for exercise and 2 for food: "))
    if entry_type not in [1, 2]:
        print("Invalid input. Please enter 1 or 2.")
        return

    if person_number == 1:
        log_entry("anu", entry_type)
    elif person_number == 2:
        log_entry("simon", entry_type)
    elif person_number == 3:
        log_entry("john", entry_type)
    else:
        print("Invalid person number.")


def retrieve_person_data(person_number):
    '''
    Retrieve and display data for a specified person and entry type.
    :param person_number:
        (int)The number of the person whose data is being retrieved.
    :return:
        None
    Example:
        >>> retrieve_person_data(1)
        Enter 1 for exercise and 2 for food: 1
        2024-06-06 14:30:00: Ran 5 miles in the morning.
        2024-06-06 15:45:00: Did weight training at the gym.

    Note:
        - The function prompts the user to enter 1 for exercise-related data and 2 for food-related data.
        - Depending on the person number provided,
          the function retrieves and displays the data for the corresponding person using the retrieve_entry function.
    '''
    entry_type = int(input("Enter 1 for exercise and 2 for food: "))
    if entry_type not in [1, 2]:
        print("Invalid input. Please enter 1 or 2.")
        return

    if person_number == 1:
        retrieve_entry("anu", entry_type)
    elif person_number == 2:
        retrieve_entry("simon", entry_type)
    elif person_number == 3:
        retrieve_entry("john", entry_type)
    else:
        print("Invalid person number.")


def log_personal_info(person):
    '''
    Log personal information for a specified person into a text file.
    :param person:
        (str)The name of the person for whom personal information is being logged.
    :return:
        None
    Example:
        >>> log_personal_info("Smith")
        Enter gender: Male
        Enter height (in cm): 175
        Enter weight (in kg): 70
        Personal information logged successfully

    Note:
        - The function prompts the user to input gender, height (in cm), and weight (in kg) for the specified person.
        - The information is written to a text file named "{person}-info.txt".
    '''
    filename = f"{person}-info.txt"

    gender = input("Enter gender: ")
    height = input("Enter height (in cm): ")
    weight = input("Enter weight (in kg): ")

    with open(filename, "w") as file:
        file.write(f"Gender: {gender}\n")
        file.write(f"Height: {height} cm\n")
        file.write(f"Weight: {weight} kg\n")

    print("Personal information logged successfully")


def retrieve_personal_info(person):
    '''
    Retrieve and display personal information for a specified person from a text file.
    :param person:
        (str)The name of the person whose personal information is being retrieved.
    :return:
        None
    Example:
        >>> retrieve_personal_info("Smith")
        Gender: Male
        Height: 175 cm
        Weight: 70 kg

    Note:
        - The function retrieves personal information from a text file named "{person}-info.txt".
        - If the file exists, the function reads and displays the information.
        - If the file does not exist,
          a message indicating that no personal information is found for the person is displayed.
    '''
    filename = f"{person}-info.txt"

    if os.path.exists(filename):
        with open(filename, "r") as file:
            print(file.read())
    else:
        print(f"No personal information found for {person}")


def main():
    while True:
        print("Health Management System")
        print("1. Log exercise or food entry")
        print("2. Retrieve exercise or food entry")
        print("3. Log personal information")
        print("4. Retrieve personal information")
        print("5. Exit")

        action = int(input("Choose an option: "))

        if action not in [1, 2, 3, 4, 5]:
            print("Invalid input. Please enter a valid option.")
            continue

        if action == 5:
            break

        person_number = int(input("Press 1 for Anu, 2 for Simon, 3 for John: "))

        if action == 1:
            input_person_data(person_number)
        elif action == 2:
            retrieve_person_data(person_number)
        elif action == 3:
            if person_number == 1:
                log_personal_info("anu")
            elif person_number == 2:
                log_personal_info("simon")
            elif person_number == 3:
                log_personal_info("john")
            else:
                print("Invalid person number.")
        elif action == 4:
            if person_number == 1:
                retrieve_personal_info("anu")
            elif person_number == 2:
                retrieve_personal_info("simon")
            elif person_number == 3:
                retrieve_personal_info("john")
            else:
                print("Invalid person number.")


if __name__ == "__main__":
    main()
