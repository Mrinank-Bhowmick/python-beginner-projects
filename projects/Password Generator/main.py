import random
import string

print("Welcome to this Password Generator")

# Set the password length with constraints for the password length
password_length = int(input("\nEnter the length of password: "))

while password_length < 8:
    print("Your password must have at least 8 characters")
    password_length = int(input("\nEnter the length of password: "))

# define the characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all_characters = lower + upper + num + symbols

# generate a password string
temp = random.sample(all_characters, password_length)
password = "".join(temp)

# print password
print("Your password is: " + password)
print("Thanks for using the Password Generator")
