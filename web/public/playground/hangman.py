# Hangman
# Guess the hidden word one letter at a time before you run out of tries.

import random

words = ["python", "browser", "rocket", "puzzle", "guitar", "planet", "coffee"]
word = random.choice(words)

guessed = set()
tries = 6

print("Welcome to Hangman! Guess the word, one letter at a time.")
print(f"The word has {len(word)} letters.")
print()

while tries > 0:
    shown = " ".join(letter if letter in guessed else "_" for letter in word)
    print("Word:   ", shown)
    print("Tries left:", tries)

    if all(letter in guessed for letter in word):
        print("\nYou win! 🎉 The word was:", word)
        break

    guess = input("Guess a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please type a single letter.\n")
        continue

    if guess in guessed:
        print("You already tried that one.\n")
        continue

    guessed.add(guess)

    if guess in word:
        print("Good guess!\n")
    else:
        tries -= 1
        print("Nope, that letter isn't in the word.\n")
else:
    print("\nOut of tries! 😅 The word was:", word)
