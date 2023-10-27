import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="susername", passwd="password")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists students")
mycursor.execute("use students")
mycursor.execute(
    "create table if not exists studentsinfo(sch_no int(50),name char(100),age int(50),email varchar(150),phone varchar(150))"
)
mycursor.execute("create table if not exists admin(id char(100),password varchar(150))")
mydb.commit()


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    var1 = str(input("Enter the sch no. of the student:"))
    var2 = str(input("Enter the name of the student:"))
    var3 = str(input("Enter the age of the student:"))
    var4 = str(input("Enter the email of the student:"))
    var5 = str(input("Enter the phone no. of the student:"))
    mycursor.execute(
        "insert into studentsinfo values('"
        + var1
        + "','"
        + var2
        + "','"
        + var3
        + "','"
        + var4
        + "','"
        + var5
        + "')"
    )
    mydb.commit()
    print("Data saved successfully!")
    input("Press Enter to continue!")
    display_menu()
    return


def view_students():
    print("------------------------")
    print("--- Student Records ---")
    print("------------------------")
    mycursor.execute("select * from studentsinfo")
    for i in mycursor:
        print(i)
    input("Press Enter to continue!")
    display_menu()
    return


def search_student():
    print("------------------------")
    print("--- Search Student ---")
    print("------------------------")
    a = input("Enter the sch no. of the student:")
    mycursor.execute("select * from studentsinfo where Sch_no=('" + a + "')")
    result = mycursor.fetchall()
    if len(result) == 0:
        print("Enter valid sch no.!")
    else:
        for i in result:
            print(i)
    input("Press Enter to continue!")
    display_menu()
    return


def update_student():
    print("------------------------")
    print("--- Update Student ---")
    print("------------------------")
    var1 = input("Enter the sch no. of the student:")
    var2 = str(input("Enter the name of the student:"))
    var3 = str(input("Enter the age of the student:"))
    var4 = str(input("Enter the email of the student:"))
    var5 = str(input("Enter the phone no. of the student:"))
    mycursor.execute(
        "update studentsinfo set name=('"
        + var1
        + "'),age=('"
        + var2
        + "'),email=('"
        + var3
        + "'),phone=('"
        + var4
        + "') where Sch_no=('"
        + var5
        + "')"
    )
    mydb.commit()
    print("Data updated successfully!")
    input("Press Enter to continue!")
    display_menu()
    return


def delete_student():
    print("------------------------")
    print("--- Delete Student ---")
    print("------------------------")
    var1 = input("Enter the sch no. of the student:")
    mycursor.execute("delete from studentsinfo where sch_no=('" + var1 + "')")
    mydb.commit()
    print("Data deleted successfully!")
    input("Press Enter to continue!")
    display_menu()
    return


def exit_program():
    print("---------------------------------")
    print(" Thank you for using our system!")
    print("    Created by Siddharth Jain")
    print("       Have a nice day :)")
    print("---------------------------------")


def display_menu():
    print("1: Add New Student")
    print("2: View Students")
    print("3: Search Student")
    print("4: Update Student")
    print("5: Delete Student")
    print("6: Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        exit_program()
    else:
        print("invalid")


def register():
    print("-------------------------")
    print("--------Register---------")
    print("-------------------------")
    id = str(input("Enter your Id:"))
    password = str(input("Enter your Password:"))
    mycursor.execute("insert into admin values('" + id + "','" + password + "')")
    mydb.commit()
    print("Registered successfully!")
    input("Press Enter to continue!")
    login()
    return


def login():
    print("-------------")
    print("--- login ---")
    print("-------------")
    id = input("Enter the id:")
    password = input("Enter the password:")
    mycursor.execute(
        "select * from admin where id=('" + id + "') and password=('" + password + "')"
    )
    result = mycursor.fetchall()
    if len(result) == 1:
        print("-------------------------------------")
        print("--Welcome", id, "what you want to do!--")
        print("-------------------------------------")
        display_menu()
    else:
        print("Enter valid Id and Password!")
        login()


def start():
    print("-------------------------------------")
    print(" Welcome to Student Management System")
    print("-------------------------------------")
    print("1: Login")
    print("2: Register")
    choice = input("Enter your choice: ")
    if choice == "1":
        login()
    elif choice == "2":
        register()


start()
