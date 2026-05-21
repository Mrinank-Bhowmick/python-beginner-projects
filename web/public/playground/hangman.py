# === Hangman · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @Mrinank-Bhowmick.

import random

# Pick a random secret word from the list
words = ["python", "browser", "rocket", "puzzle", "guitar", "planet", "coffee"]
word = random.choice(words)

# Track guessed letters and remaining tries
guessed = set()
tries = 6

# Welcome the player and show word length
print("Welcome to Hangman! Guess the word, one letter at a time.")
print(f"The word has {len(word)} letters.")
print()

# Keep looping while tries remain
while tries > 0:
    shown = " ".join(letter if letter in guessed else "_" for letter in word)
    print("Word:   ", shown)
    print("Tries left:", tries)

    # Check if the player has won
    if all(letter in guessed for letter in word):
        print("\nYou win! 🎉 The word was:", word)
        break

    guess = input("Guess a letter: ").strip().lower()

    # Reject input that is not a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please type a single letter.\n")
        continue

    # Skip already-tried letters
    if guess in guessed:
        print("You already tried that one.\n")
        continue

    guessed.add(guess)

    # Give feedback and deduct a try if wrong
    if guess in word:
        print("Good guess!\n")
    else:
        tries -= 1
        print("Nope, that letter isn't in the word.\n")
else:
    print("\nOut of tries! 😅 The word was:", word)
