def bookbuy():
    print("success buy")


def booksell():
    print("success sell")


def canteen():
    print("success canteen")


def helpdesk():
    print("success helped")


def healthcare():
    print("success health")


def notice():
    print("success notice")


def exit():
    res = messagebox.askyesnocancel("Notification", "Do you want to exit?")
    if res == True:
        root.destroy()


#################################################################################
def connectdb():
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry("500x500+780+200")
    dbroot.resizable(False, False)
    #########################################box label
    idlabel = Label(dbroot, text="Name:", width=20, anchor="c")
    idlabel.place(x=10, y=10)
    rolllabel = Label(dbroot, text="Roll:", width=20, anchor="c")
    rolllabel.place(x=10, y=50)
    ########################################userentry
    nameentry = Entry(dbroot, font=("arial", 10, "bold"), textvariable="StringVar()")
    nameentry.place(x=250, y=10)
    rollentry = Entry(dbroot, font=("arial", 10, "bold"), textvariable="StringVar()")
    rollentry.place(x=250, y=50)
    #########################################button
    submitbutton = Button(dbroot, text="SUBMIT", width=20)
    submitbutton.place(x=200, y=130)

    dbroot.mainloop()


############################################################################
from tkinter import *
from tkinter import Toplevel, messagebox
import time

root = Tk()
root.title("college system")
root.configure(bg="blue")
root.geometry("1107x700+200+50")
root.resizable(False, False)
####################################################################frame
dataframe = Frame(root, bg="white", relief=GROOVE, borderwidth=2)
dataframe.place(x=10, y=100, width=500, height=550)
#####################################################################frame1button
bookbuy = Button(dataframe, text="BOOK buy", width=25, command=bookbuy)
bookbuy.pack(side=TOP, expand=True)

booksell = Button(dataframe, text="BOOK sell", width=25, command=booksell)
booksell.pack(side=TOP, expand=True)

canteen = Button(dataframe, text="canteen", width=25, command=canteen)
canteen.pack(side=TOP, expand=True)

helpdesk = Button(dataframe, text="helpdesk", width=25, command=helpdesk)
helpdesk.pack(side=TOP, expand=True)

healthcare = Button(dataframe, text="healthcare", width=25, command=healthcare)
healthcare.pack(side=TOP, expand=True)

notice = Button(dataframe, text="notice", width=25, command=notice)
notice.pack(side=TOP, expand=True)

exit = Button(dataframe, text="exit", width=25, command=exit)
exit.pack(side=TOP, expand=True)


######################################################################secondframe
showframe = Frame(root, bg="white", relief=GROOVE, borderwidth=2)
showframe.place(x=550, y=100, width=550, height=550)
######################################################################heading
titlelabel = Label(
    root,
    text="COLLEGE SYSTEM",
    font=("arial", 30, "bold"),
    relief=GROOVE,
    borderwidth=2,
    bg="gold2",
)
titlelabel.place(x=400, y=10)
########################################################################connectdatabase
connectbutton = Button(root, text="Database", width=23, height=3, command=connectdb)
connectbutton.place(x=900, y=10)


root.mainloop()
