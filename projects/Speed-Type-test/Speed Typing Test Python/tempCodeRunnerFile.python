from tkinter import *                                                   #importing the tkinter module

def btnClick(numbers):                                                  # to display on the calculator screen when user clicks a button 
    global operator                                                     #declaring a global variable
    operator = operator + str(numbers)
    text_Input.set(operator)                                            #prints the clicked button on the screen
    
def btnClear():                                                         #when user hits the clear button
    global operator
    operator=""
    text_Input.set("")                                                  # clears the display field

def btnEquals():
    global operator
    sumup=str(eval(operator))                                           #eveluating the result of the expression using eval()
    text_Input.set(sumup)                                               #displays the result to the screen
    operator=""                                                         #clears the variable for further input
    
cal = Tk()                                                              #callng the Tk() class / creates an instance of Tk()
cal.title("Calculator")                                                 #creating a title for the main window
operator=""
text_Input= StringVar()

#==========================================================================================================================================================
#creating graphics for the calculator


txtDisplay = Entry(cal, font=('arial', 20,"bold"), textvariable=text_Input, bd=30, insertwidth=4,bg="powder blue", justify="right").grid(columnspan=4)

btn7=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="7", command=lambda:btnClick(7), bg="powder blue").grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="8", command=lambda:btnClick(8),bg="powder blue").grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="9",command=lambda:btnClick(9),bg="powder blue").grid(row=1,column=2)
btn_add=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="+",command=lambda:btnClick("+"),bg="powder blue").grid(row=1,column=3)

btn4=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="4",command=lambda:btnClick(4),bg="powder blue").grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="5",command=lambda:btnClick(5),bg="powder blue").grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="6",command=lambda:btnClick(6),bg="powder blue").grid(row=2,column=2)
btn_times=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="*",command=lambda:btnClick("*"),bg="powder blue").grid(row=2,column=3)

btn1=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="1",command=lambda:btnClick(1),bg="powder blue").grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnClick(2),bg="powder blue").grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="3",command=lambda:btnClick(3),bg="powder blue").grid(row=3,column=2)
btn_minus=Button(cal,padx=16,bd=8, fg="black",font=('arial',20,'bold'),text="-",command=lambda:btnClick("-"),bg="powder blue").grid(row=3,column=3)

btn0=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="0",command=lambda:btnClick(0),bg="powder blue").grid(row=4,column=0)
btn_clear=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="C",bg="powder blue",command=btnClear).grid(row=4,column=1)
btn_equals=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="=",bg="powder blue",command=btnEquals).grid(row=4,column=2)
btn_div=Button(cal,padx=16,pady=16,bd=8, fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnClick("/"),bg="powder blue").grid(row=4,column=3)

#=============================================================================================================================================================
cal.mainloop()