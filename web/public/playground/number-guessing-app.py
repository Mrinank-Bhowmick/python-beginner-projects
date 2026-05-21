# === Number Guessing App · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @cypherab01.

# Import random to generate secret numbers
import random


# Define the player-guesses mode
def guess():
    # Pick a secret number between 1 and 20
    n = random.randrange(1, 20)

    # Ask the player for their first guess
    var_guess = int(input("Enter any number: "))

    # Keep looping until the guess matches
    while n != var_guess:
        if var_guess < n:
            print("OOPS! Too low")
            # Ask for another guess
            var_guess = int(input("Guess again: "))
        elif var_guess > n:
            print("OOPS! Too high!")
            # Ask for another guess
            var_guess = int(input("Guess again: "))
        else:
            break

    # Congratulate the player on a correct guess
    print(f"Congratulations!! You guessed the number {n} correctly")


# Define the computer-guesses mode
def computer_guess():
    global comp_guess

    # Ask the player to pick a secret number
    x = int(input("Enter your number: "))

    # Set initial search range for the computer
    low = 1
    high = x

    # Track player feedback each round
    comp_ans = ""

    # Loop until the computer gets it right
    while comp_ans != "c":
        if low != high:
            # Pick a random number within the current range
            comp_guess = random.randint(low, high)
        else:
            comp_guess = (
                low
            )

        # Show the guess and get player feedback
        comp_ans = input(
            f"Is {comp_guess} too high (h), too low (l), or correct (c)? \n=>"
        ).lower()

        # Narrow the range based on feedback
        if comp_ans == "h":
            high = comp_guess - 1
        elif comp_ans == "l":
            low = comp_guess + 1

    # Announce the computer found the number
    print(f"Yay! The computer guessed your number, {comp_guess}, correctly!")


if __name__ == "__main__":
    # Show the mode selection menu
    print(
        "Select gaming mode\n Press 1 to guess the number\nPress 2 to choose the number"
    )
    g_mode = int(input())

    # Run the chosen game mode
    if g_mode == 1:
        guess()
    if g_mode == 2:
        computer_guess()
