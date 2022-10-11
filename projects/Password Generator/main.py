import random
import string


def main():
    print("_____________________________________")
    print("| Welcome to this Password Generator |")
    print("-------------------------------------\n")
    password_length = 0
    while password_length < 8:
        print("Your password must have at least 8 characters")
        password_length = getPasswordLength()

    all_characters = getCharacters()
    password = generatePassword(all_characters, password_length)
    print("\nYour password is: " + password)
    print("__________________________________________")
    print("| Thanks for using the Password Generator |")
    print("------------------------------------------")


def getPasswordLength():
    # Set the password length with constraints for the password length
    password_length = int(input("\nEnter the length of password: "))
    return password_length


def getCharacters():
    # define the characters
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all_characters = lower + upper + num + symbols
    return all_characters


def generatePassword(all_characters, password_length):
    # generate a password string
    password = "".join(random.sample(all_characters, password_length))
    return password


main()
