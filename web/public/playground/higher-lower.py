# === Higher-Lower Game · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ZackeryRSmith.

from random import randint

# Welcome message and pick the secret number
print("Welcome to the Higher-Lower Game!")
rnum = randint(0, 100)
noguesses = 0

# Keep looping until the player wins
while True:

    # Keep asking until a valid integer is entered
    while True:
        guess = input("Guess the number: ")
        if guess.isdigit():
            integer_number = int(guess)
            print("You entered:", integer_number)

            # Tell the player to go higher, lower, or celebrate a win
            if integer_number > rnum:
                print("Lower")
            elif integer_number < rnum:
                print("Higher")
            else:
                (print("You win! the number is " + guess + "!"), quit())
            noguesses += 1
        else:
            print("Invalid input. Please enter an integer number.")
