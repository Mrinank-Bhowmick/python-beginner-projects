"""
Text Editor -
Notepad style application that can open, edit, and save text documents. 
Optional: Add syntax highlighting and other features.
"""

from tkinter import *
from tkinter.filedialog import (
    askopenfile,
    asksaveasfile,
    askopenfilename,
    asksaveasfilename,
)
import os
from pygments import highlight

counter = 1


class TextEditor:
    def donothing(self):
        self.filewin = Toplevel(self.root)
        button = Button(self.filewin, text="Do not do anything")
        button.pack()

    def open_file(self):
        self.file = askopenfile(mode="r")
        if self.file is not None:
            self.text.delete(1.0, "end-1c")
            content = self.file.read()
            self.filename = self.file.name
            self.text.insert(INSERT, content)
            self.filename_only = self.filename.split("/")[-1]
            self.root.title(self.filename_only + "-TryCatch Text Editor")

    def save_file(self):
        if self.filename != None and self.file != None:
            f = open(self.filename, "r+")
            f.seek(0)
            f.truncate()
            self.text_data = self.text.get(1.0, "end-1c")
            f.write(self.text_data)

        else:
            self.file = asksaveasfile()
            self.filename = self.file.name
            self.text_data = self.text.get(1.0, "end-1c")
            f = open(self.filename, "r+")
            f.write(self.text_data)
            self.filename_only = self.filename.split("/")[-1]
            self.root.title(self.filename_only + "-TryCatch Text Editor")

    def save_as_file(self):
        self.file = asksaveasfile()
        self.filename = self.file.name
        self.text_data = self.text.get(1.0, "end-1c")
        f = open(self.filename, "r+")
        f.write(self.text_data)
        self.filename_only = self.filename.split("/")[-1]
        self.root.title(self.filename_only + "-TryCatch Text Editor")

    def close_file(self):
        self.text.delete(1.0, "end-1c")
        self.root.title("Untitled" + "-TryCatch Text Editor")
        self.file.close()
        self.file = None
        self.filename = None

    def new(self):
        global counter, win

        counter += 1
        win[counter] = TextEditor()

    def dark(self):
        self.text.config(
            foreground="white", background="black", insertbackground="white"
        )

    def light(self):
        self.text.config(
            foreground="black", background="white", insertbackground="black"
        )

    def __init__(self):
        self.root = Tk()

        # Adding Scorll Bar
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.root.title("Untitled-TryCatch Text Editor")

        self.file = None
        self.filename = None

        # Adding Menu Bar
        menubar = Menu(self.root)
        self.filemenu = Menu(menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.new)
        self.filemenu.add_command(label="Open", command=self.open_file)
        self.filemenu.add_command(label="Save", command=self.save_file)
        self.filemenu.add_command(label="Save as...", command=self.save_as_file)
        self.filemenu.add_command(label="Close", command=self.close_file)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=self.filemenu)

        editmenu = Menu(menubar, tearoff=0)
        # editmenu.add_command(label="Undo", command=self.donothing)
        # editmenu.add_separator()
        # editmenu.add_command(label="Cut", command=self.donothing)
        # editmenu.add_command(label="Copy", command=self.donothing)
        # editmenu.add_command(label="Paste", command=self.donothing)
        # editmenu.add_command(label="Delete", command=self.donothing)
        # editmenu.add_command(label="Select All", command=self.donothing)
        editmenu.add_command(label="Dark", command=self.dark)
        editmenu.add_command(label="Light", command=self.light)
        menubar.add_cascade(label="Theme", menu=editmenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.root.config(menu=menubar)

        # Adding Text field
        self.text = Text(self.root)
        self.text.pack()
        self.text.tag_add("here", "1.0", "1.4")
        self.text.tag_add("start", "1.8", "1.13")
        self.text.tag_config("here", background="yellow", foreground="blue")
        self.text.tag_config("start", background="aqua", foreground="green")
        self.text.config(insertbackground="black")

        self.photo = PhotoImage(file="Projects-1/edit-text.png")
        self.root.iconphoto(False, self.photo)

        # Running GUI application
        self.root.mainloop()


# print(filename)
win = dict()

"""
For initial, we have created an instance of Class Text editor and stored that instance in dictionary
Then if user clicks on new then a new instance is created and appended in dictionary.
"""
win[counter] = TextEditor()
