# === Morse Code Translator · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ZackeryRSmith.

# Lookup table mapping letters/digits to Morse symbols
MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ", ": "--..--",
    ".": ".-.-.-",
    "?": "..--..",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
}


# Convert a plain-text message to Morse code
def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            cipher += " "

    return cipher


# Convert a Morse code message back to plain text
def decrypt(message):
    # Append trailing space so last code gets processed
    message += " "

    decipher = ""
    citext = ""
    for letter in message:
        if letter != " ":
            i = 0

            # Accumulate dots and dashes for one character
            citext += letter

        else:
            i += 1

            # Two spaces mark a word boundary
            if i == 2:
                decipher += " "
            else:
                # Reverse-lookup the Morse sequence
                decipher += list(MORSE_CODE_DICT.keys())[
                    list(MORSE_CODE_DICT.values()).index(citext)
                ]
                citext = ""

    return decipher


# Run a hard-coded demo: encode then decode a name
def main():
    message = "Mrinank-Bhowmick"
    result = encrypt(message.upper())
    print(result)

    message = "-- .-. .. -. .- -. -.- -....- -... .... --- .-- -- .. -.-. -.-"
    result = decrypt(message)
    print(result)


if __name__ == "__main__":
    main()
