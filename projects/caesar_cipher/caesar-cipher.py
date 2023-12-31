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
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    new_word = []
    new_sentence = []
    text = text.split()
    for words in text:
        for chosen_letter in words:
            i = 0
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


def decrypt(text, shift):
    alphabet.reverse()
    new_word = []
    new_sentence = []
    text = text.split()
    for words in text:
        for chosen_letter in words:
            i = 0
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


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
