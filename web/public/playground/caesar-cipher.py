# === Caesar Cipher · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @Harry830.

# Define the alphabet used for shifting
alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
# Get direction, message, and shift from user
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Shift each letter forward to encrypt the message
def encrypt(text, shift):
    new_word = []
    new_sentence = []
    text = text.split()
    for words in text:
        for chosen_letter in words:
            i = 0
            # Find the letter and shift its position forward
            for letter in alphabet:
                if chosen_letter == letter:
                    new_shift = i + shift
                    new_shift = new_shift % 26
                    position = alphabet[new_shift]
                    new_word.append(position)
                i = i + 1
        new_word = "".join(new_word)
        new_sentence.append(new_word)
        new_word = []
    new_sentence = " ".join(new_sentence)
    print(f"the encoded message is {new_sentence}")


# Shift each letter backward to decrypt the message
def decrypt(text, shift):
    alphabet.reverse()
    new_word = []
    new_sentence = []
    text = text.split()
    for words in text:
        for chosen_letter in words:
            i = 0
            # Find the letter in reversed alphabet and shift
            for letter in alphabet:
                if chosen_letter == letter:
                    new_shift = i + shift
                    new_shift = new_shift % 26
                    position = alphabet[new_shift]
                    new_word.append(position)
                i = i + 1
        new_word = "".join(new_word)
        new_sentence.append(new_word)
        new_word = []
    new_sentence = " ".join(new_sentence)
    print(f"the decoded message is {new_sentence}")
    alphabet.reverse()


# Run encrypt or decrypt based on user's choice
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
