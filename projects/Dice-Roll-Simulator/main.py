import random


def roll_dice():
    """Simulates rolling a 6-sided dice and prints the result."""
    number = random.randint(1, 6)
    print("You rolled:", number)


def main():
    while True:
        print("1. Roll the dice")
        print("2. Exit")
        user_choice = input("What do you want to do? ")

        if user_choice == "1":
            roll_dice()
        elif user_choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
