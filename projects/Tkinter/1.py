import tkinter as tk
from tkinter import ttk

LARGEFONT = ("Times New Roman", 35)


class tkinterApp(tk.Tk):
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (std_ca, LandPage, accnt, lgin):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2, page3 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(std_ca)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame["bg"] = "sea green"
        frame.tkraise()


# Student and College authority categorization


class std_ca(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Label of frame layout 1
        label_lp = ttk.Label(
            self,
            text="You are Student or College Authority ?",
            font=("Times New Roman", 36),
        )
        label_lp.place(x=400, y=100)
        button_std = ttk.Button(
            self, text="Student", command=lambda: controller.show_frame(LandPage)
        )
        button_std.place(x=550, y=200, height=60, width=150)

        button_ca = ttk.Button(
            self,
            text="College Authority",
            command=lambda: controller.show_frame(LandPage),
        )
        button_ca.place(x=800, y=200, height=60, width=150)


# first window frame startpage


class LandPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label of frame Layout 2
        label = ttk.Label(self, text="Welcome..!!", font=LARGEFONT)
        label1 = ttk.Label(self, text="New User? Create New Account", font=24)
        label.place(x=620, y=10)
        label1.place(x=620, y=100)

        button1 = ttk.Button(
            self,
            text="Create New Account",
            command=lambda: controller.show_frame(accnt),
        )
        button1.place(x=550, y=200, height=60, width=150)

        button2 = ttk.Button(
            self, text="Login", command=lambda: controller.show_frame(lgin)
        )
        button2.place(x=800, y=200, height=60, width=150)

        button_back = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame(std_ca)
        )
        button_back.place(x=680, y=300, height=60, width=150)


# second window frame page1
class accnt(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Create your account", font=LARGEFONT)
        label.grid(row=0, column=6, padx=10, pady=10)
        # Name
        label_name = ttk.Label(
            self, text="Enter your Name:", font=("Times New Roman", 14)
        )
        label_name.grid(row=1, column=4, padx=10, pady=10)
        entry_name = ttk.Entry(self, width=25, font=("Times New Roman", 12))
        entry_name.grid(row=1, column=5, padx=10, pady=10)
        str_name = entry_name.get()
        # email
        label_mail = ttk.Label(
            self, text="Enter your email:", font=("Times New Roman", 14)
        )
        label_mail.grid(row=1, column=6, padx=10, pady=10)
        entry_mail = ttk.Entry(self, width=25, font=("Times New Roman", 12))
        entry_mail.grid(row=1, column=7, padx=10, pady=10)
        str_mail = entry_mail.get()
        # dept
        ttk.Label(self, text="Select Department", font=("Times New Roman", 14)).grid(
            row=3, column=4, padx=10, pady=25
        )
        n = tk.StringVar()
        dept_chs = ttk.Combobox(self, width=10, textvariable=n)
        dept_chs["values"] = (" ECE", " CSE", " ME", " CE", " EE", " AIE", " IT")
        dept_chs.grid(row=3, column=5)
        dept_chs.current()
        # College roll
        label_roll = ttk.Label(
            self, text="Enter your Roll No.:", font=("Times New Roman", 14)
        )
        label_roll.grid(row=3, column=6, padx=10, pady=10)
        entry_roll = ttk.Entry(self, width=25, font=("Times New Roman", 12))
        entry_roll.grid(row=3, column=7, padx=10, pady=10)
        str_roll = entry_mail.get()
        # year
        ttk.Label(self, text="Select current year:", font=("Times New Roman", 14)).grid(
            row=4, column=4, padx=10, pady=25
        )
        n = tk.StringVar()
        dept_chs = ttk.Combobox(self, width=10, textvariable=n)
        dept_chs["values"] = (" 1st", " 2nd", " 3rd", " 4th")
        dept_chs.grid(row=4, column=5)
        dept_chs.current()
        # gender
        ttk.Label(self, text="Enter Gender:", font=("Times New Roman", 14)).grid(
            row=5, column=4, padx=10, pady=10
        )
        var = tk.IntVar()
        r1 = ttk.Radiobutton(self, text="Male", variable=var, value=1)
        r1.grid(row=5, column=5, padx=10, pady=25)
        r1 = ttk.Radiobutton(self, text="Female", variable=var, value=2)
        r1.grid(row=5, column=6, padx=10, pady=25)
        r1 = ttk.Radiobutton(self, text="Others", variable=var, value=2)
        r1.grid(row=5, column=7, padx=10, pady=25)
        # declaration
        chk = ttk.Checkbutton(
            self,
            text="I hereby declare that all the informations provided are correct. ",
        )
        chk.grid(row=7, column=5, padx=10, pady=10)
        # password
        label_pass = ttk.Label(
            self, text="Enter your Password:", font=("Times New Roman", 14)
        )
        label_pass.grid(row=6, column=4, padx=10, pady=10)
        entry_pass = ttk.Entry(self, width=25, font=("Times New Roman", 12), show="*")
        entry_pass.grid(row=6, column=5, padx=10, pady=10)
        str_pass = entry_pass.get()

        # Return home
        button1 = ttk.Button(
            self,
            text="Return to Home page",
            command=lambda: controller.show_frame(LandPage),
        )
        button1.grid(row=8, column=6, padx=10, pady=10)
        # Submission
        button1 = ttk.Button(self, text="Submit")
        button1.grid(row=8, column=5, padx=10, pady=10)


# third window frame page2
class lgin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # ttk.configure(bg='blue')
        label = ttk.Label(self, text="Login ", font=LARGEFONT)
        label.place(x=650, y=100)
        # name entry label
        label_name = ttk.Label(
            self, text="Enter your Name:", font=("Times New Roman", 14)
        )
        label_name.place(x=500, y=200)
        # enter name
        entry_name = ttk.Entry(self, width=25, font=("Times New Roman", 12))
        entry_name.place(x=700, y=200)
        str_name = entry_name.get()
        # label_password
        label_pass = ttk.Label(
            self, text="Enter your Password:", font=("Times New Roman", 14)
        )
        label_pass.place(x=500, y=250)
        # enter password
        entry_pass = ttk.Entry(self, width=25, font=("Times New Roman", 12), show="*")
        entry_pass.place(x=700, y=250)
        str_pass = entry_pass.get()
        # check box
        # rob_check=ttk.IntVar()
        chk = ttk.Checkbutton(self, text="I am not a robot")
        chk.place(x=600, y=300, height=50, width=250)
        # back button
        button2 = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame(LandPage)
        )
        button2.place(x=600, y=400, height=50, width=100)
        # submit button
        button3 = ttk.Button(self, text="Submit")
        button3.place(x=750, y=400, height=50, width=100)


# Driver Code
app = tkinterApp()
# app['bg']='blue'
app.mainloop()
