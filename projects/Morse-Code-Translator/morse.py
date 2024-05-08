# Dictionary for Morse code
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


def encrypt(text):
    text = text.upper()  # Convert the input to uppercase
    cipher = ""
    for letter in text:
        if letter != " ":
            if letter in morse_code:
                # Looks up the dictionary and adds the
                # corresponding Morse code
                # along with a space to separate
                # Morse codes for different characters
                cipher += morse_code[letter] + " "
            else:
                # If the character is not in the dictionary, add a space
                cipher += " "
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += " "

    return cipher


# Function to decrypt the string
# from Morse to English
def decrypt(text):
    # extra space added at the end to access the
    # last Morse code
    text += " "

    decipher = ""
    citext = ""
    for letter in text:
        # checks for space
        if letter != " ":
            # counter to keep track of space
            i = 0

            # storing Morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1, that indicates a new character
            i += 1

            # if i = 2, that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher += " "
            else:
                # accessing the keys using their values (reverse of encryption)
                for char, code in morse_code.items():
                    if code == citext:
                        decipher += char
                        break
                citext = ""

    return decipher


choice = input(
    "Enter 'E' for encryption (text to Morse code) or 'D' for decryption (Morse code to text): "
)

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
