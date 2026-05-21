# === Pig Latin Converter · annotated for the pyBegin playground ===
# Note: the project's function.py helper is inlined below so this runs as a
# single self-contained file in the browser playground.


# Convert an English sentence into Pig Latin
def to_pig(eng_string):
    eng_words = eng_string.split()
    pig_words = []
    vowels = ["a", "e", "i", "o", "u"]
    cap_vowels = ["A", "E", "I", "O", "U"]

    # Transform each word in turn
    for word in eng_words:
        for i in range(len(word)):
            # Words starting with a vowel just get "yay"
            if word[0] in vowels or word[0] in cap_vowels:
                pig_words.append(word + "yay")
                break

            # Capitalised words: move letters and keep the title case
            elif word[0].isupper():
                if word[i] in vowels or word[0] in cap_vowels:
                    remain = word[i:].title()
                    pig_words.append(remain + word[:i].lower() + "ay")
                    break

            # Other words: move the leading consonants and add "ay"
            else:
                if word[i] in vowels or word[0] in cap_vowels:
                    pig_words.append(word[i:] + word[:i] + "ay")
                    break

    # Join the converted words back into a sentence
    pig_sentence = " ".join(pig_words)
    return pig_sentence


# Greet the user and show a separator
print("Hello! Welcome to a Pig Latin converter")
print("=" * 39)

# Ask user for the string to convert
original_string = input(
    "Please type the string you would like to convert to pig latin: "
)

# Print the converted Pig Latin result
print()
print("Your converted string is:")
print(to_pig(original_string))
