import random
import string

def generate_password(length, use_numbers=True, use_symbols=True):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if length < 6:
        print("Password length should be at least 6 characters for security.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password: "))
    use_numbers = input("Include numbers (yes/no)? ").strip().lower() == 'yes'
    use_symbols = input("Include symbols (yes/no)? ").strip().lower() == 'yes'

    password = generate_password(length, use_numbers, use_symbols)

    if password:
        print(f"Your random password is: {password}")
    else:
        print("Password generation failed. Please try again.")

if __name__ == "__main__":
    main()
