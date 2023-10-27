import random
import os


while True:
    global answer_y

    # Clears the shell/terminal (where all the text is)
    os.system("clear")

    answer = input("Pick a side for the coin toss: ")

    list1 = ["heads", "tails"]

    # Picks randonly from the list
    random_s = random.choice(list1)

    print("You got... " + random_s)

    if answer.lower() == random_s:
        # Tells the user if they won
        print("Nice you won the coin toss!!")

        # Asks the user if they want to play again
        answer_y = input("Wanna play agian? ")
        if answer_y.lower() == "no":
            break

    if answer.lower() != random_s:
        # Tells the user if they lost
        print("OOF.")

        # Asks the user if they want to play again
        answer_y = input("Wanna play agian? ")
        if answer_y.lower() == "no":
            break
