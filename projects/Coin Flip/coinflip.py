import random
import os


def toss_coin():
    list1 = ["heads", "tails"]
    return random.choice(list1)


def main():
    while True:
        # Clears the shell/terminal (where all the text is)
        os.system("cls")

        answer = input("Pick a side for the coin toss (heads/tails): ")

        # Input validation
        if answer.lower() not in ["heads", "tails"]:
            print("Invalid input. Please enter 'heads' or 'tails'.")
            continue

        result = toss_coin()

        print(f"You got... {result}")

        if answer.lower() == result:
            print("Nice, you won the coin toss!!")
        else:
            print("OOF. Better luck next time.")

        # Ask the user if they want to play again
        answer_y = input("Wanna play again? (yes/no): ")
        if answer_y.lower() != "yes":
            break


if __name__ == "__main__":
    main()


# while True:
#     global answer_y
#
#     # Clears the shell/terminal (where all the text is)
#     os.system("clear")
#
#     answer = input("Pick a side for the coin toss: ")
#
#     list1 = ["heads", "tails"]
#
#     # Picks randonly from the list
#     random_s = random.choice(list1)
#
#     print("You got... " + random_s)
#
#     if answer.lower() == random_s:
#         # Tells the user if they won
#         print("Nice you won the coin toss!!")
#
#         # Asks the user if they want to play again
#         answer_y = input("Wanna play agian? ")
#         if answer_y.lower() == "no":
#             break
#
#     if answer.lower() != random_s:
#         # Tells the user if they lost
#         print("OOF.")
#
#         # Asks the user if they want to play again
#         answer_y = input("Wanna play agian? ")
#         if answer_y.lower() == "no":
#             break
