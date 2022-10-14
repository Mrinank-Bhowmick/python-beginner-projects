
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    guess = str()
    for char in secret_word:
      for letter in letters_guessed:
        if char == letter:
          guess += char
        else:
         continue
    
    if guess == secret_word:
        return True
    else:
        return False

    


def get_guessed_word(secret_word, letters_guessed):
    output_list = []
    for char in secret_word:
      output_list.append("_ ")
    for letter in letters_guessed:
        for count, char in enumerate(secret_word):
          if char == letter:
            output_list[count] = letter
          else:
            continue
    
    output_string = "".join(output_list)
    return output_string


def get_available_letters(letters_guessed):
    avail_letters_list = []
    alphabets = list(string.ascii_lowercase)
    
    for letters in letters_guessed:
     alphabets.remove(letters)

    alphabets_str = ''.join(alphabets)        
    return alphabets_str
    

def hangman(secret_word):
    left_guesses = 6
    warning = 3
    good_guess = 0
    lengeth = len(secret_word)
    print("Welcome to the game Hangman!")
    print ("I am thinking of a word that is", lengeth, "letters long." )
    print("----------------------")
    letters_guessed = []
    while not is_word_guessed(secret_word, letters_guessed) and left_guesses > 0:
      print("You have", left_guesses, "guesses left.")
      print("Available letters:" + get_available_letters(letters_guessed))
      entered = str.lower(input("Please guess a letter: "))
      if entered not in string.ascii_lowercase:
        warning -= 1
      if entered in letters_guessed:
        warning -= 1
        print ("Oops! You've already guessed that letter. You now have", warning ,"warnings")
      elif warning == 0:
        left_guesses -= 1
      else:
        letters_guessed.append(entered)
        if entered not in secret_word:
          left_guesses -= 1
          print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
        else:
          print("Good guess", get_guessed_word(secret_word, letters_guessed))
          good_guess += 1           
      
      print("-----------------------------------------------------")
    if is_word_guessed(secret_word, letters_guessed):
      print("Congratulations, you won!")
      print("Your Total score is: ", (left_guesses*good_guess))
    else:
      print("Sorry, you ran out of guesses. The word was: ", secret_word)  

secret_word = choose_word(wordlist)
hangman(secret_word)