import random

from RandomWords import easy_wordlist, medium_wordlist, hard_wordlist

DIFFICULTY_LEVEL = "medium"


def hangman(tries):
    """
    List of Symbolic representation of losing the tries / for wrong attempts
    (THE HANGMAN)
    """
    stages = [
        """
        # final state 
                           --------
                           |      |
                           |      O
                           |     \\|/
                           |      ||
                           |     // \\
                           -
                        """,
        """
        # head, torso, four legs, four arms
                           --------
                           |      |
                           |      O
                           |     \\|/
                           |      |
                           |     // \\
                           -
                        """,
        #  head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def get_word():
    """
    easy_wordlist (list): list of words (strings) - for easy difficulty level
    medium_wordlist (list): list of words (strings) - for medium difficulty level
    hard_wordlist (list): list of words (strings) - for hard difficulty level

    Returns a word from wordlist at random
    """
    if DIFFICULTY_LEVEL == "easy":
        word = random.choice(easy_wordlist)
    elif DIFFICULTY_LEVEL == "medium":
        word = random.choice(medium_wordlist)
    elif DIFFICULTY_LEVEL == "hard":
        word = random.choice(hard_wordlist)
    else:
        word = random.choice(medium_wordlist)
    return word.upper()


def choose_difficulty():
    global DIFFICULTY_LEVEL
    DIFFICULTY_LEVEL = input("Choose difficulty level (easy, medium, hard): ").lower()
    if DIFFICULTY_LEVEL == "easy":
        return (
            8  # we can adjust the number of initial guesses for each difficulty level
        )
    elif DIFFICULTY_LEVEL == "medium":
        return 6
    elif DIFFICULTY_LEVEL == "hard":
        return 4
    else:
        print("Invalid difficulty level. Defaulting to medium.")
        return 6


def play(word, initial_tries):
    """
      Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []

    tries = initial_tries

    print("\n-------------Welcome to Hangman-------------\n")
    print(hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Guess the word:- ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("An incorrect guess.")
        print(hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")

    else:
        print("Sorry, you ran out of tries. The word was " + word + ". play again :)")


def main():
    """
    * This triggers the game by asking for intialization
    """
    difficulty = choose_difficulty()
    word = get_word()
    play(word, difficulty)
    while input("Do you want to play Hangman? (y/n): ").upper() == "Y":
        difficulty = choose_difficulty()
        word = get_word()
        play(word, difficulty)


if __name__ == "__main__":
    main()
