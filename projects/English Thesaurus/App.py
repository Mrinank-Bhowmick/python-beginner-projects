"""
Title:English_Thesaurus

"""

import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

# Loads the dictionary data from data.json file
data = json.load(open("projects\English Thesaurus\data.json"))


def eng_thesaurus(word):
    word = word.lower()

    # Checks for the exact word in data dictionary
    if word in data:
        found = data[word]
        for i in range(0, len(found)):
            if i == 0:
                print("Meaning 1:", found[i])
            else:
                print("Meaning " + str(i + 1) + ":", found[i])

    # If word entered has an incorrect spelling
    else:
        # Matches with the word with the closet spelling
        closet_word = get_close_matches(word, data.keys(), cutoff=0.75)
        for j in range(0, len(closet_word)):
            print("Did u mean the word", closet_word[j], "?\n")
            op = input("Press Yes-Y,No-N,Exit-E:")
            x = data[closet_word[j]]
            if op == "Y":
                for k in range(0, len(x)):
                    print("Meaning " + str(k + 1), ":", x[k])
                break
            elif op == "N":
                print(
                    "ERROR : Word doesn't exist!! Please double check the entered word"
                )
                break
            elif op == "E":
                exit


print("\nCtrl-C to exit")
while True:
    eng_thesaurus(input("\nEnter the word to find meaning:"))
