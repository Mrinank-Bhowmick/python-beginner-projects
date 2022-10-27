from tkinter import messagebox
from tkinter import *
import json
from passgen import generatedpass


def searc():
    try:
        with open("data.json", "r") as f:
            d = json.load(f)
            p = d[webinput.get()]["password"]
            e = d[webinput.get()]["email"]
            messagebox.showinfo(
                title=f"{webinput.get()}", message=f"Email is {e} \n password is {p}"
            )

    except KeyError:
        messagebox.showinfo(title="Not Found", message="Data not found")
    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="File missing")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    passinput.insert(0, generatedpass())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savedata():
    website = webinput.get()
    email = emailinput.get()
    passwo = passinput.get()
    new_data = {website: {"email": email, "password": passwo}}
    if emailinput.get() == "" or webinput.get() == "" or passinput.get() == "":
        messagebox.showinfo(
            title="Warning", message="Please fill all the enteries to proceed"
        )
    else:
        is_ok = messagebox.askokcancel(
            title=webinput.get(),
            message=f"Check all details \n Password : {passinput.get()} \n email : {emailinput.get()} ",
        )
        if is_ok:
            try:
                with open("data.json", "r") as f:
                    data = json.load(f)
                    data[website] = new_data[website]
                with open("data.json", "w") as f:
                    json.dump(data, f, indent=4)
            except:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)

            emailinput.delete(0, END)
            webinput.delete(0, END)
            passinput.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Managger")
window.config(padx=50, pady=50)
canva = Canvas(width=200, height=200)
log = PhotoImage(file="logo.png")
canva.create_image(100, 100, image=log)
canva.grid(row=0, column=1)

website = Label(text="Website")
website.grid(row=1, column=0)

email = Label(text="Email")
email.grid(row=2, column=0)

Password = Label(text="Password")
Password.grid(row=3, column=0)

webinput = Entry(width=30)
webinput.grid(row=1, column=1)

emailinput = Entry(width=30)
emailinput.grid(row=2, column=1)

passinput = Entry(width=30)
passinput.grid(row=3, column=1)

genbtn = Button(text="genetrate", command=generator)
genbtn.grid(row=3, column=2)

add = Button(text="ADD", width=36, command=savedata)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", command=searc)
search.grid(row=1, column=2)

window.mainloop()
