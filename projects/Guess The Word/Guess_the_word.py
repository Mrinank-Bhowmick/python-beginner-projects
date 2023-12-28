import random

# List of words for the game
word_list = [
    "python",
    "java",
    "javascript",
    "ruby",
    "php",
    "html",
    "css",
    "csharp",
    "angular",
    "golang",
    "c",
    "dotnet",
    "perl",
    "rust",
    "scala",
    "dart",
    "fortran",
    "cobol",
    "haskell",
]


# Function to choose a random word from the list
def choose_random_word(word_list):
    return random.choice(word_list)


# Function to play the word guessing game
def word_guessing_game():
    word_to_guess = choose_random_word(word_list)
    guessed_letters = []
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("You have 6 attempts to guess the word.")
    print("_ " * len(word_to_guess))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Correct guess!")
            remaining_letters = [
                letter if letter in guessed_letters else "_" for letter in word_to_guess
            ]
            print(" ".join(remaining_letters))
            if "_" not in remaining_letters:
                print("Congratulations! You've guessed the word:", word_to_guess)
                break
        else:
            attempts -= 1
            if attempts < 3:
                print(f"It is a name of a programming language")
            print(f"Wrong guess. You have {attempts} attempts remaining.")

    if attempts == 0:
        print("You've run out of attempts. The word was:", word_to_guess)


# Start the game
word_guessing_game()
