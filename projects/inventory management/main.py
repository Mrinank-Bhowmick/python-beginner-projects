import tkinter
import mysql.connector as q

con = q.connect(host="localhost", user="root", passwd="", database="records")
cursor = con.cursor()

# Adding record to an empty table(inventory)


def ADD():
    pid = int(input("Enter the product id:"))
    pname = input("Enter the product name: ")
    pcost = int(input("Enter the product cost:"))
    pqty = int(input("Enter the product quantity:"))
    query = "insert into inventory values({},'{}',{},{})".format(
        pid, pname, pcost, pqty
    )
    cursor.execute(query)
    con.commit()
    print("Data Inserted successfully")


# Displaying record in List form


def Display():
    cursor.execute("select * from inventory")
    record = cursor.fetchall()
    print("ID", " ", "Name", " ", "Cost", "", "Quantity")
    for i in record:
        print(i)
    print("Total Number of record=", cursor.rowcount)


# Searching product on the basis of product code


def Search():
    val = int(input("Enter the product code to search:"))
    flag = 0
    cursor.execute("select * from inventory")
    record = cursor.fetchall()
    for i in record:
        if i[0] == val:
            flag = 1
            print("ID", " ", "Name", " ", "Cost", "", "Quantity")
            print(i)
    if flag == 0:
        print("---Record not found---")


# Updating existing record on the basis of product ID


def Update():
    code = int(input("Enter the product id to update:"))
    pid = int(input("Enter product id:"))
    pname = input("Enter product name:")
    pcost = int(input("Enter the product cost:"))
    pqty = int(input("Enter the product quantity:"))
    query = (
        "update inventory set PID={},PNAME='{}',PCOST={},PQTY={} where PID={}".format(
            pid, pname, pcost, pqty, code
        )
    )
    cursor.execute(query)
    con.commit()
    print("Data Updated SuccessfullY")


# Deleting records


def Delete():
    val = int(input("Enter product ID whose records are to be deleted:"))
    query = "delete from inventory where PID={}".format(val)
    cursor.execute(query)
    con.commit()
    if cursor.rowcount > 0:
        print("Record Successfully Deleted")
    else:
        print("Product not found")


def check():
    if e1.get() == "Admin" and e2.get() == "1234":
        win = tkinter.Tk()
        win.title("Inventory")
        win.configure(bg="SteelBlue1")
        win.geometry("500x400")
        login.destroy()
        l = tkinter.Label(
            win,
            text="Welcome to Super Market",
            font=("Arial", 18, "bold"),
            bg="SteelBlue1",
            fg="Black",
        )
        l.pack(side="top")
        search = tkinter.Button(
            win, text="Search", font=("Arial", 10, "bold"), command=Search, bg="azure"
        )
        add = tkinter.Button(
            win, text="  Add  ", font=("Arial", 10, "bold"), command=ADD, bg="azure"
        )
        update = tkinter.Button(
            win, text="Update", font=("Arial", 10, "bold"), command=Update, bg="azure"
        )
        display = tkinter.Button(
            win, text="Display", font=("Arial", 10, "bold"), command=Display, bg="azure"
        )
        delete = tkinter.Button(
            win, text=" Delete ", font=("Arial", 10, "bold"), command=Delete, bg="azure"
        )
        e = tkinter.Button(
            win,
            text="  Exit  ",
            font=("Arial", 10, "bold"),
            command=win.destroy,
            bg="azure",
        )
        add.place(x=90, y=100)
        display.place(x=90, y=200)
        search.place(x=300, y=100)
        update.place(x=195, y=150)
        delete.place(x=300, y=200)
        e.place(x=200, y=250)
        win.mainloop()

    else:
        l1 = tkinter.Label(
            login,
            text="Login Unsuccessful!!",
            font=("Arial", 10, "bold"),
            fg="black",
            bg="light salmon",
        )
        l1.place(x=110, y=170)


login = tkinter.Tk()
login.geometry("400x220")
login.configure(bg="light salmon")
login.title("Authorised Login Only")
o = tkinter.Label(
    login, text="Login", font=("Arial", 18, "bold"), bg="light salmon", fg="black"
)
o.pack(side="top")

l1 = tkinter.Label(login, text="Username", font=("Arial", 10, "bold"), bg="white")
l1.place(x=10, y=50)
e1 = tkinter.Entry(login, width=25, font=("Arial", 10, "bold"))
e1.place(x=150, y=50)
l2 = tkinter.Label(login, text="Password", font=("Arial", 10, "bold"), bg="white")
l2.place(x=10, y=80)
e2 = tkinter.Entry(login, width=25, font=(10), show="*")
e2.place(x=150, y=80)
q = tkinter.Button(login, text="Submit", font=("Arial", 10, "bold"), command=check)
q.place(x=225, y=120)
z = tkinter.Button(
    login, text="EXIT", font=("Arial", 10, "bold"), command=login.destroy
)
z.place(x=125, y=120)
