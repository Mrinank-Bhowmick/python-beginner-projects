# Terminal based hand cricket game

import random
import time


def main():
    print("Welcome to Hand Cricket")
    print("You will be playing against the computer")
    print("You will be batting first")
    print("Enter 1 to bat, 2 to bowl")
    choice = int(input())
    if choice == 1:
        bat()
    elif choice == 2:
        bowl()
    else:
        print("Invalid choice")
        main()


def bat():
    print("You are batting")
    print("Enter a number between 1 and 6")
    print("Enter 0 to quit")
    score = 0
    while True:
        user = int(input())
        if user == 0:
            print("Your score is", score)
            break
        elif user < 1 or user > 6:
            print("Invalid input")
            continue
        else:
            comp = random.randint(1, 6)
            print("Computer chose", comp)
            if user == comp:
                print("You are out")
                print("Your score is", score)
                break
            else:
                score += user
                print("Your score is", score)


def bowl():
    print("You are bowling")
    print("Enter a number between 1 and 6")
    print("Enter 0 to quit")
    score = 0
    while True:
        comp = random.randint(1, 6)
        print("Computer chose", comp)
        user = int(input())
        if user == 0:
            print("Computer score is", score)
            break
        elif user < 1 or user > 6:
            print("Invalid input")
            continue
        else:
            if user == comp:
                print("Computer is out")
                print("Computer score is", score)
                break
            else:
                score += comp
                print("Computer score is", score)


if __name__ == "__main__":
    main()
