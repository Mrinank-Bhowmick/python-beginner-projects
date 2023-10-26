import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(host="localhost", user="username", passwd="password")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists students1")
mycursor.execute("use students1")
mycursor.execute(
    "create table if not exists studentsinfo(sch_no int(50),name char(100),age int(50),email varchar(150),phone varchar(100))"
)
mydb.commit()
for i in mycursor:
    print(i)


def display_menu():
    print("-------------------------------------")
    print(" Welcome to Student Management System")
    print("-------------------------------------")
    print("1: Add New Student")
    print("2: View Students")
    print("3: Search Student")
    print("4: Update Student")
    print("5: Delete Student")
    print("6: Quit")


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
    mycursor.execute("select * from studentsinfo where Sch_no=('" + var1 + "')")
    result = mycursor.fetchall()
    print(
        tabulate(
            result, headers=["Sch_no", "Name", "Age", "Email", "Phone"], tablefmt="psql"
        )
    )
    mydb.commit()
    print("Data saved successfully!")
    input("Press Enter to continue!")
    return


def view_students():
    print("------------------------")
    print("--- Student Records ---")
    print("------------------------")
    mycursor.execute("select * from studentsinfo;")
    result = mycursor.fetchall()
    print(
        tabulate(
            result, headers=["Sch_no", "Name", "Age", "Email", "Phone"], tablefmt="psql"
        )
    )
    input("Press Enter to continue!")
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
        print(
            tabulate(
                result,
                headers=["Sch_no", "Name", "Age", "Email", "Phone"],
                tablefmt="psql",
            )
        )
    input("Press Enter to continue!")
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
    mycursor.execute("select * from studentsinfo where Sch_no=('" + var1 + "')")
    result = mycursor.fetchall()
    if len(result) == 0:
        print("Enter valid sch no.!")
    else:
        print(
            tabulate(
                result,
                headers=["Sch_no", "Name", "Age", "Email", "Phone"],
                tablefmt="psql",
            )
        )
        print("Data updated successfully!")
    mydb.commit()
    input("Press Enter to continue!")
    return


def delete_student():
    print("------------------------")
    print("--- Delete Student ---")
    print("------------------------")
    var1 = input("Enter the sch no. of the student:")
    mycursor.execute("delete from studentsinfo where sch_no=('" + var1 + "')")
    mycursor.execute("select * from studentsinfo where Sch_no=('" + var1 + "')")
    result = mycursor.fetchall()
    if len(result) == 0:
        print("Data deleted successfully!")
    else:
        print(
            tabulate(
                result,
                headers=["Sch_no", "Name", "Age", "Email", "Phone"],
                tablefmt="psql",
            )
        )
    mydb.commit()
    input("Press Enter to continue!")
    return


while True:
    display_menu()

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
    else:
        break

print("---------------------------------")
print(" Thank you for using our system!")
print("    Created by Siddharth Jain")
print("       Have a nice day :)")
print("---------------------------------")
