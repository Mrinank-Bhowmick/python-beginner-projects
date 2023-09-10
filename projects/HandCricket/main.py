# Terminal based hand cricket game

import random
import time


def main():
    print("Welcome to Hand Cricket")
    print("You will be playing against the computer")
    print("Enter 1 to bat first, 2 to bowl first")
    try:
        choice = int(input())
        if choice == 1:
            our_score = bat()
            computers_score = bowl()
            who_won(our_score, computers_score)

        elif choice == 2:
            computers_score = bowl()
            our_score = bat()
            who_won(our_score, computers_score)
        else:
            print("Invalid choice")
            main()
    except Exception as e:
        print("Invalid choice,exiting game")
        print(e)


def who_won(our_score, computers_score):
    print()
    print("Match Result")
    print("===========")
    print("You scored=", our_score)
    print("Computer scored=", computers_score)
    if our_score > computers_score:
        print("You won")
    elif computers_score > our_score:
        print("You lost")
    else:
        print("You Drew")
    print("Thank you for playing and have a good day :) ")


def bat():
    print()
    print("You are batting")
    print("Rules")
    print("=====")
    print("You need to chose a number and the computer chooses a number")
    print("If they are the same you are out")
    print("If they are different you score some runs")
    print()
    print("Game start")
    print("=========")
    score = 0
    while True:
        print("Enter a number between 1 and 6 or Enter 0 to quit")
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
                print()
                print("You are out")
                print("Your score is", score)
                input("press enter to continue")
                break
            else:
                score += user
                print("Your score is", score)
    return score


def bowl():
    print("You are bowling")
    print("Rules")
    print("=====")
    print("You need to chose a number and the computer chooses a number")
    print("If they are the same you bowl the computer out")
    print("If they are different the computer scores runs")
    print()
    print("Game start")
    print("=========")
    score = 0
    while True:
        print("Enter a number between 1 and 6 or Enter to quit")
        user = int(input())
        comp = random.randint(1, 6)
        print("Computer chose", comp)
        if user == 0:
            print("Computer score is", score)
            break
        elif user < 1 or user > 6:
            print("Invalid input")
            continue
        else:
            if user == comp:
                print()
                print("Computer is out")
                print("Computer score is", score)
                input("press enter to continue")
                break
            else:
                score += comp
                print("Computer score is", score)
    return score


if __name__ == "__main__":
    main()
