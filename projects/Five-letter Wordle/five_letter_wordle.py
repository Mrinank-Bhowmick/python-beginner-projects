import random
url = "https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').lower().split()


def play():  
  # Game instruction
  print("""Welcome to Wordle!
You have six attempts 
Progress Guide:  
✔: Letter at that position was guessed correctly 
➕: Letter is in the hidden word, but in a different position 
❌: Letter isn't in the hidden word
Good luck! """) 
  
  # Randomly generate a 5-letter word
  hidden_word = random.choice(words)
  attempt = 6
  
  while attempt > 0:
    guess = str(input("\nEnter your guess: "))

    # Check if your guess is a valid 5-letter word 
    if len(guess) != 5 or not guess.isalpha():
        print("Please enter a valid 5-letter word.")
        continue

    # If your guess is correct, you win!
    elif guess == hidden_word:
      print("Congratulations! You guessed the word! {hidden_word}")
      break

    # If your guess is incorrect, display your current progess
    else:
      attempt -= 1
      print(f"You have {attempt} attempt(s) remaining")
      for c, w in zip(hidden_word, guess):
            if w in hidden_word and w in c:
                print(" ✔ ", end = '')
            elif w in hidden_word:
                print(" ➕ ", end = '')
            else:
                print(" ❌ ", end = '')
      if attempt == 0:
        print("\nGame over! ")
        print(f"The word is {hidden_word} ")

play()
