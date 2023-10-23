# Import Module 
from tkinter import *

# Create Object 
root = Tk() 

# Set geometry 
root.geometry('400x500') 

# Add Buttons, Label, ListBox 
Name = StringVar() 
Number = StringVar() 

frame = Frame() 
frame.pack(pady=10) 

frame1 = Frame() 
frame1.pack() 

frame2 = Frame() 
frame2.pack(pady=10) 

Label(frame, text = 'Name', font='arial 12 bold').pack(side=LEFT) 
Entry(frame, textvariable = Name,width=50).pack() 

Label(frame1, text = 'Phone No.', font='arial 12 bold').pack(side=LEFT) 
Entry(frame1, textvariable = Number,width=50).pack() 

Label(frame2, text = 'Address', font='arial 12 bold').pack(side=LEFT) 
address = Text(frame2,width=37,height=10) 
address.pack() 

Button(root,text="Add",font="arial 12 bold").place(x= 100, y=270) 
Button(root,text="View",font="arial 12 bold").place(x= 100, y=310) 
Button(root,text="Delete",font="arial 12 bold").place(x= 100, y=350) 
Button(root,text="Reset",font="arial 12 bold").place(x= 100, y=390) 

scroll_bar = Scrollbar(root, orient=VERTICAL) 
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12) 
scroll_bar.config (command=select.yview) 
scroll_bar.pack(side=RIGHT, fill=Y) 
select.place(x=200,y=260) 

# Execute Tkinter 
root.mainloop()
