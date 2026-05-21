# === Love Calculator · annotated for the pyBegin playground ===

import random
import time

CONSONANTS = "bcdfghjklmnprstvwxyz"
VOWELS = "aeiou"


# Count how many vowels are in a name
def count_vowels(name):
    # Initialize vowel_counts to 0
    vowels_count = 0

    # Iterate over each letter in the name
    for letter in name.lower():
        # Check if the letter is a vowel
        if letter in VOWELS:
            vowels_count += 1

    return vowels_count


# Count how many consonants are in a name
def count_consonants(name):
    # Initialize an empty list to store consonants
    consonants_list = []

    # Iterate over each letter in the name
    for letter in name:
        # Check if the letter is a consonant
        if len(letter.lower()) == 1 and letter.lower() in CONSONANTS:
            consonants_list.append(letter)

    return len(consonants_list)


# Compute a love score from two names
def calculate_love_score(name1, name2):
    # Initialize love score to 0
    love = 0

    # Compare total vowels in both names
    total_vowel1 = count_vowels(name1)
    total_vowel2 = count_vowels(name2)

    if total_vowel1 == total_vowel2:
        love += random.randint(10, 30)

    # Compare total consonants in both names
    consonants1 = count_consonants(name1)
    consonants2 = count_consonants(name2)

    if consonants1 == consonants2:
        love += random.randint(
            20, 40
        )

    # Compare first letters of both names
    if name1.split()[0][0] == name2.split()[0][0]:
        love += random.randint(
            10, 30
        )

    # Compare the lengths of both names
    if len(name1) == len(name2):
        love += random.randint(1, 10)

    # Add a random score to love score
    love += random.randint(10, 50)

    return min(love, 100)


# Print the score and describe the relationship
def display_relationship(name1, name2, love):
    print("Calculating...")
    time.sleep(random.randint(1, 3))
    print(f"{name1} and {name2} have a {love}% relationship.")

    # Show a message based on the score range
    if love >= 90:
        print("They have an unbreakable relationship that will last forever.")
    elif 70 <= love < 90:
        print(
            "They have a strong relationship that will most likely lead to a marriage."
        )
    elif 50 <= love < 70:
        print("They have a good relationship that can lead to a honeymoon to Paris.")
    else:
        print(
            "They have a weak relationship that could have been a 'match made in heaven'."
        )


if __name__ == "__main__":
    # Ask the user for two names
    name1 = input("Please type Name 1.\n")
    name2 = input("Please type Name 2.\n")

    # Calculate and display the love score
    love_score = calculate_love_score(name1, name2)
    display_relationship(name1, name2, love_score)
