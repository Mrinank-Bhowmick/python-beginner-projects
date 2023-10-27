import time
f_name = ["" for _ in range(50)]
s_name = ["" for _ in range(50)]
gender = ["" for _ in range(50)]
age = ["" for _ in range(50)]
height = ["" for _ in range(50)]
weight = ["" for _ in range(50)]
hair_color = ["" for _ in range(50)]
eye_color = ["" for _ in range(50)]
crime = ["" for _ in range(50)]
contact = ["" for _ in range(50)]
cell_no = list(range(11, 61))
num = 0

MAX_ATTEMPTS = 3

credentials = {
    "maheen": "hehehe",
    "ayesha": "ayeshahere",
    "iqra": "iqra1",
}

attempts = 0

def display_menu():
    print("Time:", time.strftime("%H:%M:%S"))
    print("\n" * 3)
    print(" " * 70 + "*****************************")
    print(" " * 65 + "PRISON MANAGEMENT SYSTEM")
    print(" " * 70 + "*****************************")

def login():
    global attempts
    print("\n" * 2)
    print(" " * 70 + "----------------------------------")
    print(" " * 70 + "|          SYSTEM LOGIN          |")
    print(" " * 70 + "----------------------------------")
    print("\n" * 2)
    username = input(" " * 60 + "Enter a username: ")
    password = input(" " * 60 + "Enter a password: ")
    
    if credentials.get(username) == password:
        print(" " * 60 + "Access granted.")
    else:
        attempts += 1
        if attempts < MAX_ATTEMPTS:
            print(" " * 60 + f"Invalid username or password. {MAX_ATTEMPTS - attempts} attempts remaining.")
            login()
        else:
            print(" " * 60 + "Too many invalid attempts.")
            exit()

while True:
    display_menu()
    print("\n" + " " * 60 + "1) New prisoner entry")
    print(" " * 60 + "2) Prisoner list")
    print(" " * 60 + "3) Search prisoner")
    print(" " * 60 + "4) Prison File")
    print(" " * 60 + "5) Logout")
    print(" " * 60 + "6) Exit")
    option = int(input(" " * 65 + "Enter your choice: "))

    if option == 1:
        print("Time:", time.strftime("%H:%M:%S"))
        print("\n" + " " * 60 + "------------------------------------------------------")
        print(" " * 60 + "|         Enter basic details of the prisoner        |")
        print(" " * 60 + "------------------------------------------------------")
        f_name[num] = input("Enter First name: ")
        s_name[num] = input("Enter Second name: ")
        gender[num] = input("Enter Gender: ")
        age[num] = input("Enter Age: ")
        height[num] = input("Enter Height: ")
        weight[num] = input("Enter Weight: ")
        hair_color[num] = input("Enter Hair color: ")
        eye_color[num] = input("Enter Eye color: ")
        crime[num] = input("Enter crime: ")
        contact[num] = input("Enter Emergency Contact: ")
        print("Cell number is:", cell_no[0])
        cell_no[0] += 1
        num += 1
    elif option == 2:
    
        print("\n" + " " * 60 + "Prisoner List")
        print(" " * 60 + "-------------------")
        for i in range(num):
            if f_name[i] != "":
                print(f"{i + 1}. {f_name[i]} {s_name[i]}, Cell Block: {cell_no[i]}, Age: {age[i]}, Gender: {gender[i]}, Height: {height[i]}, Eye Colour: {eye_color[i]}, Crime: {crime[i]}")
        if num == 0:
            print("No prisoners in the list.")
    elif option == 3:
        # Search for a prisoner
        search_cell = int(input("Enter the cell number to search: "))
        if search_cell in cell_no:
            idx = cell_no.index(search_cell)
            print(f"{f_name[idx]} {s_name[idx]}, Cell Block: {cell_no[idx]}, Age: {age[idx]}, Gender: {gender[idx]}, Height: {height[idx]}, Eye Colour: {eye_color[idx]}, Crime: {crime[idx]}")
        else:
            print("Invalid cell number.")
    elif option == 4:
        # Save data to a file (you can choose the format)
        file_format = input("Enter the file format (e.g., txt, html, doc): ")
        filename = "Prison_Data." + file_format
        with open(filename, "w") as file:
            for i in range(num):
                if f_name[i] != "":
                    file.write(f"Name: {f_name[i]} {s_name[i]}, Cell Block: {cell_no[i], Age: {age[i]}, Gender: {gender[i]}, Height: {height[i]}, Eye Colour: {eye_color[i]}, Crime: {crime[i]}\n")
        print(f"{file_format.upper()} file created successfully.")
    elif option == 5:
        # Logout
        print("Logging out...")
        time.sleep(2)
        attempts = 0
    elif option == 6:
        # Exit the program
        print("Thank you!\nGoodbye!\nTake Care!")
        break
    else:
        print("Invalid option. Please try again.")
