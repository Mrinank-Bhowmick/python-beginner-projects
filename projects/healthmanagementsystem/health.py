import datetime


def gettime():
    return datetime.datetime.now()


def inputt(n):
    if n == 1:
        d = int(input("Enter 1 for excerise and 2 for food :"))
        if d == 1:
            value = input("type here.. \n")
            with open("anu-exe.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
        elif d == 2:
            value = input("type here.. \n")
            with open("anu-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
    elif n == 2:
        d = int(input("Enter 1 for exercise and 2 for food :"))
        if d == 1:
            value = input("type here.. \n")
            with open("simon-exe.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
        elif d == 2:
            value = input("type here.. \n")
            with open("simon-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
    elif n == 3:
        d = int(input("Enter 1 for exercise and 2 for food :"))
        if d == 1:
            value = input("type here.. \n")
            with open("john-exe.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
        elif d == 2:
            value = input("type here.. \n")
            with open("john-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n ")
            print("written successfully ")
    else:
        print("Enter the valid input 1(anu) 2(simon) 3(john)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("anu-exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("anu-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("simon-exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("simon-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("john-exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("john-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (anu,simon,john)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for anu 2 for simon 3 for john "))
    inputt(b)
else:
    b = int(input("Press 1 for anu 2 for simon 3 for john "))
    retrieve(b)
