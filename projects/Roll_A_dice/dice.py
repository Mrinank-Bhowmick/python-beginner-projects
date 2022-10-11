# importing modules

import random
import mysql.connector

# setting up mysql connection
mydb = mysql.connector.connect(
    host="localhost",
    user="yourUsername",
    passwd="yourPassword",
    database="databaseName",
)
mycursor = mydb.cursor()

name = input("Your name: ")
print("Hey " + name + "! Welcome to Roll A Dice game🎲 ")
print(
    """Rules: 
1. You have to roll a dice. 
2. Whatever number comes in, an associated task will be given to you. 
3. You have to perform the task. 
4. After you're done, press enter. 
5. Don't forget to have fun🥳 
"""
)

n = int(
    input(
        """Choose any one: 
    1. Move ahead with the game 
    2. Exit 
    """
    )
)
if n == 1:
    num = random.randint(1, 6)
    print("🎲 - ", num)
    if num == 1:
        print(
            """Yayyyy!! You got 1!.
        Your task is to name your favourite movie"""
        )
        ans = input("Your ans: ")
        print("Woaah! Cool")
    elif num == 2:
        print(
            """Yayyyy!! You got 2!.
        What would you prefer, Mountains or beach?"""
        )
        ans = input("Your ans: ")
        print("Nice choice")
    elif num == 3:
        print(
            """Yayyyy!! You got 3!.
        Name 3 of your favourite Indian food"""
        )
        ans = input("Your ans: ")
        a = ["Sounds Delicious", "Yummy", "Tasty", "I got watery mouth 🍉"]
        print(random.choice(a))
    elif num == 4:
        print(
            """Yayyyy!! You got 4!.
            When Joe was 6 years old, his little brother John was half of his age.
            If Joe is 40 years old today, how old is John?"""
        )
        ans = int(input())
        if ans == 37:
            print("Viola! You are right")
        else:
            print("Oops! You are wrong! The correct answer is 37.")

    elif num == 5:
        print(
            """Yayyyy!! You got 5!.
         What has two banks but no money🤔?"""
        )
        ans = input("Your ans: ")
        if ans == "River bank" or ans == "river bank":
            print("Viola! You are right")
        else:
            print("Oops! You are wrong! The correct answer is River bank")

    elif num == 6:
        print(
            """Yayyyy!! You got 6!.
        Name the six continents of the World"""
        )
        list = []
        for i in range(0, 6):
            ans = input("Enter element: ")
            list.append(ans)
        print("You entered: ", list)
    print("Have a good day!")
else:
    print("Sayonara! See you soon")
    exit()

# inserting value in database
sql = "INSERT INTO tableName VALUES (%s, %s,%s)"
val = (name, num, ans)
mycursor.execute(sql, val)

mydb.commit()

print("Your response has been recorded ✅!")
