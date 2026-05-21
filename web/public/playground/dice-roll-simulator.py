# === Dice Rolling Simulator · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ZackeryRSmith.

import random


# Roll a 6-sided die and print the result
def roll_dice():
    number = random.randint(1, 6)
    print("You rolled:", number)


# Show menu and handle user choice
def main():
    while True:
        print("1. Roll the dice")
        print("2. Exit")
        user_choice = input("What do you want to do? ")

        # Roll if player chose 1, exit if 2
        if user_choice == "1":
            roll_dice()
        elif user_choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
