"""imports the os and time modules from the Python Standard Library.
The os module provides a way of using operating system dependent functionality, 
like reading or writing to the file system.
The time module provides various time-related functions, like getting the current 
time or pausing the execution of the script."""

import os
import time


def addition():
    """This function asks the user to enter a series of numbers separated by spaces.
    It then adds all the numbers together and returns the result."""
    nums = list(map(int, input("Enter all numbers seperated by space: ").split()))
    return sum(nums)


def subtraction():
    """This function asks the user to enter two numbers.
    It then subtracts the second number from the first and returns the result."""
    n_1 = float(input("Enter first number: "))
    n_2 = float(input("Enter second number: "))

    return n_1 - n_2


def multiplication():
    """Function asks user to enter a series of numbers separated by spaces.
    Then multiply all the numbers together and returns the result."""

    nums = list(map(int, input("Enter all numbers seperated by space: ").split()))
    result = 1
    for num in nums:
        result *= num
    return result


def division():
    """Function divide two numbers"""
    n_1 = float(input("Enter first number: "))
    n_2 = float(input("Enter second number: "))

    return n_1 / n_2


def average():
    """This function takes space seperated number series and then convert it to a list. 
    Then calculates the average of that list of numbers."""

    nums = list(map(int, input("Enter all numbers seperated by space: ").split()))
    return sum(nums) / len(nums)


C = 0
while C != "-1":
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for average")
    print("Enter '-1' to exit.\n")

    C = input("Your choice is: ")

    if C == "1":
        res = addition()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif C == "2":
        res = subtraction()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif C == "3":
        res = multiplication()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif C == "4":
        res = division()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif C == "5":
        res = average()
        os.system("cls")
        print(f"The answer is {res}")
        time.sleep(2)
        os.system("cls")

    elif C == "-1":
        os.system("cls")
        print("Thank you for using the calculator!")
        time.sleep(2)
        break

    else:
        os.system("cls")
        print("Sorry, invalid option!")
        time.sleep(2)
        os.system("cls")
