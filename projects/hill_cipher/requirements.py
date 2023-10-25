import mysql.connector as c
import string

con = c.connect(host = "localhost", user = "root", password = "_enter_password_here_")
cur = con.cursor()
cur.execute("create database hillcipher")       #database creation
cur.execute("use hillcipher")                   #useing database



#lower character table
cur.execute("create table loalpha (lid int primary key, lchar);")         #creating table
a = (string.ascii_lowercase)
for i in range(26):
    cur.execute(f"insert loalpha values({i+1},'{a[i]}');")            #inserting values



