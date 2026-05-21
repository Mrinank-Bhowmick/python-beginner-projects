# === Mastermind · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @mr-desilva.

import random

# Pick a secret 4-digit number
num = random.randrange(1000, 10000)

# Get the player's first guess
n = int(input("Guess the 4 digit number:"))

# Check if the very first guess is correct
if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    # Track how many attempts the player makes
    ctr = 0

    # Keep looping until the player guesses correctly
    while n != num:
        # Increment the attempt counter
        ctr += 1

        count = 0

        # Convert both numbers to strings for digit comparison
        n = str(n)
        num = str(num)

        # Prepare a list to show which digits were correct
        correct = ["X"] * 4

        # Compare each digit position one by one
        for i in range(0, 4):
            if n[i] == num[i]:
                count += 1
                correct[i] = n[i]
            else:
                continue

        # Tell the player how many digits they got right
        if (count < 4) and (count != 0):
            print("Not quite the number. But you did get ", count, " digit(s) correct!")
            print("Also these numbers in your input were correct.")
            for k in correct:
                print(k, end=" ")
            print("\n")
            print("\n")
            n = int(input("Enter your next choice of numbers: "))

        # Tell the player if no digits matched
        elif count == 0:
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))

    # Announce victory when the guess matches
    if n == num:
        print("You've become a Mastermind!")
        print("It took you only", ctr, "tries.")
