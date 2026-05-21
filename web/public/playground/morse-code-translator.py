# === Morse Code Translator · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ahmedalhamad7.

# Lookup table mapping letters/digits to Morse symbols
morse_code = {
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


# Convert plain text to Morse code symbols
def encrypt(text):
    text = text.upper()
    cipher = ""
    for letter in text:
        if letter != " ":
            if letter in morse_code:
                cipher += morse_code[letter] + " "
            else:
                cipher += " "
        else:
            cipher += " "

    return cipher


# Convert Morse code back to plain text
def decrypt(text):
    # Append a trailing space so the last code is processed
    text += " "

    decipher = ""
    citext = ""
    for letter in text:
        if letter != " ":
            i = 0

            # Accumulate dots and dashes for one character
            citext += letter

        else:
            i += 1

            # Two spaces mean a word boundary
            if i == 2:
                decipher += " "
            else:
                # Reverse-lookup the Morse sequence
                for char, code in morse_code.items():
                    if code == citext:
                        decipher += char
                        break
                citext = ""

    return decipher


# Ask user whether to encrypt or decrypt
choice = input(
    "Enter 'E' for encryption (text to Morse code) or 'D' for decryption (Morse code to text): "
)

# Run the chosen operation and print the result
if choice == "E":
    user_input = input("Enter the text you want to encrypt: ")
    encrypted_text = encrypt(user_input)
    print("Encrypted Morse code:", encrypted_text)

elif choice == "D":
    user_input = input(
        "Enter the Morse code you want to decrypt (separate symbols with spaces): "
    )
    decrypted_text = decrypt(user_input)
    print("Decrypted text:", decrypted_text)

else:
    print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
