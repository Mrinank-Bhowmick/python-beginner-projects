import random

from scipy import rand

letters = [
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
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

number_of_letter = random.randint(4, 6)
number_of_numbers = random.randint(4, 6)
number_of_symblos = random.randint(4, 6)

passlist = []
for i in range(number_of_letter):
    passlist.append(random.choice(letters))
for i in range(number_of_numbers):
    passlist.append(random.choice(numbers))
for i in range(number_of_symblos):
    passlist.append(random.choice(symbols))

password = ""
random.shuffle(passlist)


def generatedpass():
    for paw in passlist:
        global password
        password += paw
    return password
