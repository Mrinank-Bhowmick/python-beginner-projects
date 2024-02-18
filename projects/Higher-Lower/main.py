from random import randint

def guess_number():
    # Generate a random number between 0 and 100
    random_number = randint(0, 100) # Clear and descriptive name is a good practice (random_number instead of rnum).

    # Initialize guess number
    no_guesses = 0

    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: ")) # Prompt the user with clear message

            # Check if the guess is higher, lower, or correct
            if guess > random_number:
                print("Lower")
            elif guess < random_number:
                print("Higher")
            else:
                (print(f"You win ({no_guesses} guesses used)"), quit()) # Exit the loop when guess is correct

            # Increment the guess number
            no_guesses += 1

        except ValueError:
            print("Invalid input! Please enter a valid number (must be integer number).") # Block the invalid input by printing an error message.

if __name__ == "__main__":
    # Improve user interface by giving more information about the game.
    print("Welcome to the Number Guessing Game!")
    print("A random number is being picked between 0 and 100. Can you guess it?")
    print("A hint of 'higher' and 'lower' is provided after every guesses.")
    print("Good Luck and enjoy the game!")
    guess_number() # Game Play