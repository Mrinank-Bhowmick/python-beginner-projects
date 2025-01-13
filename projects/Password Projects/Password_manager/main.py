from tkinter import messagebox
from tkinter import *
import json
from passgen import generatedpass


def searc():
    try:
        with open("data.json", "r") as f:
            d = json.load(f)
            website = webinput.get()
            if website in d:
                email = d[website]["email"]
                password = d[website]["password"]
                
                # Update the entry fields directly
                emailinput.delete(0, END)
                emailinput.insert(0, email)
                passinput.delete(0, END)
                passinput.insert(0, password)
            else:
                messagebox.showinfo(title="Not Found", message="Data not found for the website.")
    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="Data file not found. Please save a password first.")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Error reading data file. Please check the file format.")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    passinput.delete(0, END)  # Clear previous password
    passinput.insert(0, generatedpass())


# ---------------------------- SAVE PASSWORD ------------------------------- #
def savedata():
    website = webinput.get()
    email = emailinput.get()
    passwo = passinput.get()
    new_data = {website: {"email": email, "password": passwo}}

    if not website or not email or not passwo:
        messagebox.showinfo(title="Warning", message="Please fill in all fields to proceed.")
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"Check all details\nPassword: {passwo}\nEmail: {email}"
    )

    if is_ok:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data.update(new_data)

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

        webinput.delete(0, END)
        emailinput.delete(0, END)
        passinput.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
webinput = Entry(width=30)
webinput.grid(row=1, column=1)
webinput.focus()  # Focus on website input on start

emailinput = Entry(width=30)
emailinput.grid(row=2, column=1)

passinput = Entry(width=30)
passinput.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate", command=generator)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=savedata)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", command=searc)
search_button.grid(row=1, column=2)

window.mainloop()
