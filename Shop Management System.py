pip install mysql-connector
pip install mysql-connector
#Importing the required modules
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import mysql.connector
#Connecting to the database and creating table
db=mysql.connector.connect(user="root",passwd="root",host="localhost") 
 
my_cursor=db.cursor() #getting the cursor object
my_cursor.execute("CREATE DATABASE IF NOT EXISTS Shop") #creating the database named library

db=mysql.connector.connect(user="root",passwd="root",host="localhost",database='Shop') 
my_cursor=db.cursor()
#query to create a table products
query="CREATE TABLE IF NOT EXISTS products (date VARCHAR(10),prodName VARCHAR(20), prodPrice VARCHAR(50))" 
my_cursor.execute(query) #executing the query

db=mysql.connector.connect(user="root",passwd="root",host="localhost",database='Shop') 
my_cursor=db.cursor()
#query to create a table sale
query="CREATE TABLE IF NOT EXISTS sale (custName VARCHAR(20), date VARCHAR(10), prodName VARCHAR(30),qty INTEGER, price INTEGER )" 
my_cursor.execute(query) #executing the query
#Creating the main window
wn = tkinter.Tk() 
wn.title("PythonGeeks Shop Management System")
wn.configure(bg='honeydew2')
wn.minsize(width=500,height=500)
wn.geometry("700x600")

headingFrame1 = Frame(wn,bg="snow3",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to PythonGeeks \n Shop Management System", fg='grey19', font=('Courier',15,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

#Button to add a new product
btn1 = Button(wn,text="Add a Product",bg='LightBlue1', fg='black', width=20,height=2, command=addProd)
btn1['font'] = font.Font( size=12)
btn1.place(x=270,y=175)

#Button to delete a product
btn2 = Button(wn,text="Delete a Product",bg='misty rose', fg='black',width=20,height=2,command=delProd)
btn2['font'] = font.Font( size=12)
btn2.place(x=270,y=255)

#Button to view all products
btn3 = Button(wn,text="View Products",bg='old lace', fg='black',width=20,height=2,command=viewProds)
btn3['font'] = font.Font( size=12)
btn3.place(x=270,y=335)

#Button to add a new sale and generate bill
btn4 = Button(wn,text="New Customer",bg='lavender blush2', fg='black', width=20,height=2,command = newCust)
btn4['font'] = font.Font( size=12)
btn4.place(x=270,y=415)


wn.mainloop() 
#Function to add the product to the database
def prodtoTable():
    #Getting the user inputs of product details from the user 
    pname= prodName.get()
    price = prodPrice.get()
    dt = date.get()
    #Connecting to the database
    db=mysql.connector.connect(user="root",passwd="root",host="localhost",database='Shop') 
    cursor = db.cursor()
    
    #query to add the product details to the table
    query = "INSERT INTO products(date,prodName,prodPrice) VALUES(%s,%s,%s)" 
    details = (dt,pname,price)

    #Executing the query and showing the pop up message
    try:
        cursor.execute(query,details)
        db.commit()
        messagebox.showinfo('Success',"Product added successfully")
    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Error","Trouble adding data into Database")
    
    wn.destroy()
#Function to get details of the product to be added
def addProd(): 
    global prodName, prodPrice, date, Canvas1,  wn
    
    #Creating the window
    wn = tkinter.Tk() 
    wn.title("PythonGeeks Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg='LightBlue1')
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(wn,bg='LightBlue1',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add a Product", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # Getting Date
    lable1 = Label(labelFrame,text="Date : ", fg='black')
    lable1.place(relx=0.05,rely=0.3, relheight=0.08)
        
    date = Entry(labelFrame)
    date.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.08)
        
    # Product Name
    lable2 = Label(labelFrame,text="Product Name : ", fg='black')
    lable2.place(relx=0.05,rely=0.45, relheight=0.08)
        
    prodName = Entry(labelFrame)
    prodName.place(relx=0.3,rely=0.45, relwidth=0.62, relheight=0.08)
        
    # Product Price
    lable3 = Label(labelFrame,text="Product Price : ", fg='black')
    lable3.place(relx=0.05,rely=0.6, relheight=0.08)
        
    prodPrice = Entry(labelFrame)
    prodPrice.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.08)
           
    #Add Button
    Btn = Button(wn,text="ADD",bg='#d1ccc0', fg='black',command=prodtoTable)
    Btn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)
    
    Quit= Button(wn,text="Quit",bg='#f7f1e3', fg='black',command=wn.destroy)
    Quit.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()
  #Function to remove the product from the database
def removeProd():
    #Getting the product name from the user to be removed
    name = prodName.get()
    name = name.lower()
    
    #Connecting to the database
    db=mysql.connector.connect(user="root",passwd="root",host="localhost",database='Shop') 
    cursor = db.cursor()
    
    #Query to delete the respective product from the database
    query = "DELETE from products where LOWER(prodName) = '"+name+"'"
   #Executing the query and showing the message box
    try:
        cursor.execute(query)
        db.commit()
        #cur.execute(deleteIssue)
        #con.commit()

        messagebox.showinfo('Success',"Product Record Deleted Successfully")

    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Please check Product Name")
 
    wn.destroy()
#Function to get product details from the user to be deleted
def delProd(): 

    global prodName, Canvas1,  wn
    #Creating a window
    wn = tkinter.Tk() 
    wn.title("PythonGeeks Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn)
    Canvas1.config(bg="misty rose")
    Canvas1.pack(expand=True,fill=BOTH)
    
    headingFrame1 = Frame(wn,bg="misty rose",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Delete Product", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Product Name to Delete
    lable = Label(labelFrame,text="Product Name : ", fg='black')
    lable.place(relx=0.05,rely=0.5)
        
    prodName = Entry(labelFrame)
    prodName.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Delete Button
    Btn = Button(wn,text="DELETE",bg='#d1ccc0', fg='black',command=removeProd)
    Btn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    Quit = Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()
  #Function to show all the products in the database
def viewProds():
    global  wn
    #Creating the window to show the products details
    wn = tkinter.Tk() 
    wn.title("PythonGeeks Shop Management System")
    wn.configure(bg='mint cream')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    Canvas1 = Canvas(wn) 
    Canvas1.config(bg="old lace")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(wn,bg='old lace',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Products", fg='black', font = ('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    #Connecting to database
    db=mysql.connector.connect(user="root",passwd="root",host="localhost",database='Shop') 
    cursor=db.cursor()
    #query to select all products from the table
    query = 'SELECT * FROM products'
    
    Label(labelFrame, text="%-50s%-50s%-50s"%('Date','Product','Price'),font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------",fg='black').place (relx=0.05,rely=0.2)
    #Executing the query and showing the products details
    try:
        cursor.execute(query)
        res = cursor.fetchall() 
        
        for i in res:
            Label(labelFrame,text="%-50s%-50s%-50s"%(i[0],i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
            y += 0.1
    except Exception as e:
        print("The exception is:",e)
        messagebox.showinfo("Failed to fetch files from database")
    
    Quit= Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()
  #Function to generate the bill
def bill():
    #Creating a window
    wn = tkinter.Tk() 
    wn.title("PythonGeeks Shop Management System")
    wn.configure(bg='lavender blush2')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    headingFrame1 = Frame(wn,bg="lavender blush2",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="Bill", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    
    y = 0.35
    Label(labelFrame, text="%-40s%-40s%-40s%-40s"%('Product','Price','Quantity','Total'),font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.2)
    
    #Getting date and customer name
    dt=date.get()
    cName=custName.get()
    totalBill=0
    #Connecting to database
    db=mysql.connector.connect(user="root",passwd="root",host="localhost",database='Shop') 
    cursor=db.cursor()
    #query to select all the products 
    query = 'SELECT * FROM products'
    
    #Checking if the quantity of the 1st product is entered and calculating price, showing it on window  and adding to database 
    if(len(name1.get()) != 0):
        i=res[0]
        qty=int(name1.get())
        total=qty*int(i[2])
        Label(labelFrame,text="%-40s%-40s%-40s%-40s"%(i[1],i[2],qty,total) ,fg='black').place(relx=0.07,rely=y)
        totalBill+=total
        y+=0.1
        
        query = "INSERT INTO sale(custName,date,prodName,qty,price) VALUES(%s,%s,%s,%s,%s)" 
        details = (cName,dt,i[1],qty,total)
        
    #Checking if the quantity of the 2nd product is entered and calculating price, showing it on window  and adding to database 
    if(len(name2.get()) != 0):
        i=res[1]
        qty=int(name2.get())
        total=qty*int(i[2])
        Label(labelFrame,text="%-40s%-40s%-40s%-40s"%(i[1],i[2],qty,total) ,fg='black').place(relx=0.07,rely=y)
        totalBill+=total
        y+=0.1
        query = "INSERT INTO sale(custName,date,prodName,qty,price) VALUES(%s,%s,%s,%s,%s)" 
        details = (cName,dt,i[1],qty,total)
    
    #Checking if the quantity of the 3rd product is entered and calculating price, showing it on window  and adding to database 
    if(len(name3.get()) != 0):
        i=res[2]
        qty=int(name3.get())
        total=qty*int(i[2])
        Label(labelFrame,text="%-40s%-40s%-40s%-40s"%(i[1],i[2],qty,total) ,fg='black').place(relx=0.07,rely=y)
        totalBill+=total
        y+=0.1
        query = "INSERT INTO sale(custName,date,prodName,qty,price) VALUES(%s,%s,%s,%s,%s)" 
        details = (cName,dt,i[1],qty,total)
    #showing total of the bill
    Label(labelFrame, text = "------------------------------------------------------------------------------------",fg='black').place (relx=0.05,rely=y)
    y+=0.1
    Label(labelFrame,text="\t\t\t\t\t\t\t\t"+str(totalBill) ,fg='black').place(relx=0.07,rely=y)
    
    Quit = Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    wn.mainloop()
#Function to take the inputs form the user to generate bill    
def newCust():    
    global wn,name1,name2,name3,date,custName
    #Creating a window
    wn = tkinter.Tk() 
    wn.title("PythonGeeks Shop Management System")
    wn.configure(bg='lavender blush2')
    wn.minsize(width=500,height=500)
    wn.geometry("700x600")

    headingFrame1 = Frame(wn,bg="lavender blush2",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
    headingLabel = Label(headingFrame1, text="New Customer", fg='grey19', font=('Courier',15,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    lable1 = Label(wn,text="Date : ", fg='black')
    lable1.place(relx=0.05,rely=0.3, )
        
    #Getting date
    date = Entry(wn)
    date.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    lable2 = Label(wn,text="Customer Name : ", fg='black')
    lable2.place(relx=0.05,rely=0.4, )
      
    #Getting customer name
    custName = Entry(wn)
    custName.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    labelFrame = Frame(wn)
    labelFrame.place(relx=0.1,rely=0.45,relwidth=0.8,relheight=0.4)
    
    y = 0.3
    Label(labelFrame, text="Please enter the quantity of the products you want to buy",font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.1)
    
    Label(labelFrame, text="%-50s%-50s%-30s"%('Product','Price','Quantity'),font = ('calibri',11,'bold'),
    fg='black').place(relx=0.07,rely=0.2)
    
    #Connecting to the database
    db=mysql.connector.connect(user="root",passwd="root",host="localhost",database='Shop') 
    cursor=db.cursor()
    query = 'SELECT * FROM products'

    cursor.execute(query)
    res = cursor.fetchall() 
    print(res)
    c=1
    
    #Showing all the products and creating entries to take the input of the quantity
    i=res[0]
    Label(labelFrame,text="%-50s%-50s"%(i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
    name1 = Entry(labelFrame)
    name1.place(relx=0.6,rely=y, relwidth=0.2)
    y += 0.1
    
    i=res[1]
    Label(labelFrame,text="%-50s%-50s"%(i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
    name2 = Entry(labelFrame)
    name2.place(relx=0.6,rely=y, relwidth=0.2)
    y += 0.1
    
    i=res[2]
    Label(labelFrame,text="%-50s%-50s"%(i[1],i[2]) ,fg='black').place(relx=0.07,rely=y)
    name3 = Entry(labelFrame)
    name3.place(relx=0.6,rely=y, relwidth=0.2)
    y += 0.1
    
     #Button to generate bill
    Btn= Button(wn,text="Generate Bill",bg='#d1ccc0', fg='black',command=bill)
    Btn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    Quit = Button(wn,text="Quit",bg='#f7f1e3', fg='black', command=wn.destroy)
    Quit.place(relx=0.55,rely=0.9, relwidth=0.18,relheight=0.08)

    wn.mainloop()
  
