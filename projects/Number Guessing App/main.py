# Importing the 'random' module to generate random numbers
import random


# Function to play a guessing game where the user tries to guess the number chosen by the computer
def guess():
    # Generate a random number between 1 and 20 (inclusive)
    n = random.randrange(1, 20)

    # Request user input to guess the number
    varGuess = int(input("Enter any number: "))

    # Continue the loop until the user guesses the correct number
    while n != varGuess:
        if varGuess < n:  # If the user's guess is too low
            print("OOPS! Too low")
            varGuess = int(input("Guess again: "))  # Ask for another guess
        elif varGuess > n:  # If the user's guess is too high
            print("OOPS! Too high!")
            varGuess = int(input("Guess again: "))  # Ask for another guess
        else:
            break  # Exit the loop when the correct number is guessed

    # Display a congratulatory message when the user guesses the correct number
    print(f"Congratulations!! You guessed the number {n} correctly")


# Function for the computer to guess the number chosen by the user
def computer_guess():
    global CompGuess

    # Request user input to get the number to be guessed by the computer
    x = int(input("Enter your number: "))

    # Initialize the lower and upper bounds for the computer's guessing range
    low = 1
    high = x

    # Variable to store the user's feedback on the computer's guesses
    CompAns = ""

    # Continue the loop until the computer guesses the correct number
    while CompAns != "c":
        if low != high:
            # Generate a random guess within the current range
            CompGuess = random.randint(low, high)
        else:
            CompGuess = (
                low  # If the range is reduced to a single value, guess that number
            )

        # Ask the user if the computer's guess is too high, too low, or correct
        CompAns = input(
            f"Is {CompGuess} too high (h), too low (l), or correct (c)? \n=>"
        ).lower()

        # Adjust the guessing range based on the user's feedback
        if CompAns == "h":  # If the computer's guess is too high
            high = CompGuess - 1
        elif CompAns == "l":  # If the computer's guess is too low
            low = CompGuess + 1

    # Display a message when the computer guesses the correct number
    print(f"Yay! The computer guessed your number, {CompGuess}, correctly!")


if __name__ == "__main__":
    # Display options to select the gaming mode
    print(
        "Select gaming mode\n Press 1 to guess the number\nPress 2 to choose the number"
    )
    Gmode = int(input())

    # Call the appropriate function based on the selected gaming mode
    if Gmode == 1:
        guess()
    if Gmode == 2:
        computer_guess()
