import random
import time

CONSONANTS = "bcdfghjklmnprstvwxyz"
VOWELS = "aeiou"


def count_vowels(name):
    """
    Count the number of vowels in the given name.

    Args:
        name(str): The name to count vowels in.

    Return:
        vowel_count(int): The total count of vowels in the name.
    """
    # Initialize vowel_counts to 0
    vowels_count = 0

    # Iterate over each letter in the name
    for letter in name.lower():
        # Check if the letter is a vowel
        if letter in VOWELS:
            vowels_count += 1  # add the count for each vowel

    return vowels_count  # return the total count of vowels


def count_consonants(name):
    """
    Count the number of consonants in the given name.

    Args:
        name(str): The name to count consonants in.

    Return:
        consonant_list(int): The total count of consonants in the name.
    """
    # Initialize an empty list to store consonants
    consonants_list = []

    # Iterate over each letter in the name
    for letter in name:
        # Check if the letter is a consonant
        if len(letter.lower()) == 1 and letter.lower() in CONSONANTS:
            consonants_list.append(letter)  # add the consonant to the list

    return len(consonants_list)  # return the count of consonants


def calculate_love_score(name1, name2):
    """
    Calculate a love score based on factors between two names.

    Args:
        name1(str): First name.
        name2(str): Second name.

    Return:
        love(int): Calculated of love score in percentage (0 - 100)
    """

    # Initialize love score to 0
    love = 0

    # Compare total vowels in both names
    total_vowel1 = count_vowels(name1)
    total_vowel2 = count_vowels(name2)

    if total_vowel1 == total_vowel2:
        love += random.randint(10, 30)  # add a random score if total vowels are equal

    # Compare total consonants in both names
    consonants1 = count_consonants(name1)
    consonants2 = count_consonants(name2)

    if consonants1 == consonants2:
        love += random.randint(
            20, 40
        )  # add a random score if total consonants are equal

    # Compare first letters of both names
    if name1.split()[0][0] == name2.split()[0][0]:
        love += random.randint(
            10, 30
        )  # add a random score if the first letters are equal

    # Compare the lengths of both names
    if len(name1) == len(name2):
        love += random.randint(1, 10)  # add a random score if lengths are equal

    # Add a random score to love score
    love += random.randint(10, 50)

    return min(love, 100)  # make sure final score does not exceed 100


def display_relationship(name1, name2, love):
    """
    Display the relationship details between two names based on the love score.

    Args:
        name1(str): First name.
        name2(str): Second name.
        love(int): Calculated love score.

    Return:
        None
    """
    print("Calculating...")
    time.sleep(random.randint(1, 3))
    print(f"{name1} and {name2} have a {love}% relationship.")

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
    name1 = input("Please type Name 1.\n")
    name2 = input("Please type Name 2.\n")

    love_score = calculate_love_score(name1, name2)
    display_relationship(name1, name2, love_score)
