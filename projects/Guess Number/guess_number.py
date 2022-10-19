import random

smaller_number = 1
larger_number = 10

def prompt_user():
    while True:
        try:
            user_guess = int(input(f"\nEnter number between 1 to {larger_number}: "))
            return user_guess
        except Exception as e:
            print("\nThat guess was invalid. Try again.")
    

def guess_number(user_guess):
    num = random.randint(smaller_number, larger_number)
    while num != user_guess:
        if user_guess > larger_number:
            print(f"\nYour guess exceeds the upper range. Lower your guess and try again.")
            user_guess = prompt_user()
        elif user_guess < smaller_number:
            print(f"\nYour guess is exceeds the lower range. Increase your guess and try again.")
            user_guess = prompt_user()
        elif num < user_guess:
            print(f"\nNumber is lower than {user_guess}")
            user_guess = prompt_user()
        elif num > user_guess:
            print(f"\nNumber is higher than {user_guess}")
            user_guess = prompt_user()
        else:
            print()
    print(f"\nCongrats! You've guessed the correct number! It was {num}.\n")

while True:
    play_y_n = input("Welcome to Number Guesser. If you'd like to play, press 'Y': ")
    if play_y_n.lower() == 'y':
        user_guess = prompt_user()
        guess_number(user_guess)
    else:
        print("Thanks for playing!")
        break
