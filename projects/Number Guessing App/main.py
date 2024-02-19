# Importing the 'random' module to generate random numbers
import random


# Function to play a guessing game where the user tries to guess the number chosen by the computer
def guess():
    # Generate a random number between 1 and 20 (inclusive)
    n = random.randrange(1, 20)

    # Request user input to guess the number
    var_guess = int(input("Enter any number: "))

    # Continue the loop until the user guesses the correct number
    while n != var_guess:
        if var_guess < n:  # If the user's guess is too low
            print("OOPS! Too low")
            var_guess = int(input("Guess again: "))  # Ask for another guess
        elif var_guess > n:  # If the user's guess is too high
            print("OOPS! Too high!")
            var_guess = int(input("Guess again: "))  # Ask for another guess
        else:
            break  # Exit the loop when the correct number is guessed

    # Display a congratulatory message when the user guesses the correct number
    print(f"Congratulations!! You guessed the number {n} correctly")


# Function for the computer to guess the number chosen by the user
def computer_guess():
    global comp_guess

    # Request user input to get the number to be guessed by the computer
    x = int(input("Enter your number: "))

    # Initialize the lower and upper bounds for the computer's guessing range
    low = 1
    high = x

    # Variable to store the user's feedback on the computer's guesses
    comp_ans = ""

    # Continue the loop until the computer guesses the correct number
    while comp_ans != "c":
        if low != high:
            # Generate a random guess within the current range
            comp_guess = random.randint(low, high)
        else:
            comp_guess = (
                low  # If the range is reduced to a single value, guess that number
            )

        # Ask the user if the computer's guess is too high, too low, or correct
        comp_ans = input(
            f"Is {comp_guess} too high (h), too low (l), or correct (c)? \n=>"
        ).lower()

        # Adjust the guessing range based on the user's feedback
        if comp_ans == "h":  # If the computer's guess is too high
            high = comp_guess - 1
        elif comp_ans == "l":  # If the computer's guess is too low
            low = comp_guess + 1

    # Display a message when the computer guesses the correct number
    print(f"Yay! The computer guessed your number, {comp_guess}, correctly!")


if __name__ == "__main__":
    # Display options to select the gaming mode
    print(
        "Select gaming mode\n Press 1 to guess the number\nPress 2 to choose the number"
    )
    g_mode = int(input())

    # Call the appropriate function based on the selected gaming mode
    if g_mode == 1:
        guess()
    if g_mode == 2:
        computer_guess()

