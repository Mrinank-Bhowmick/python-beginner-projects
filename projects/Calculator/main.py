import os
import time


def addition():
    nums = list(map(int, input("Enter all numbers seperated by space: ").split()))
    return sum(nums)


def subtraction():
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    return n1 - n2


def multiplication():
    nums = list(map(int, input("Enter all numbers seperated by space: ").split()))
    res = 1
    for num in nums:
        res *= num
    return res


def division():
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))

    return n1 / n2


def average():
    nums = list(map(int, input("Enter all numbers seperated by space: ").split()))
    return sum(nums) / len(nums)


c = 0
while c != "-1":
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for average")
    print("Enter '-1' to exit.\n")

    c = input("Your choice is: ")

    if c == "1":
        res = addition()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif c == "2":
        res = subtraction()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif c == "3":
        res = multiplication()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif c == "4":
        res = division()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif c == "5":
        res = average()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif c == "-1":
        os.system("cls")
        print("Thank you for using the calculator!")
        time.sleep(2)
        break

    else:
        os.system("cls")
        print("Sorry, invalid option!")
        time.sleep(2)
        os.system("cls")
