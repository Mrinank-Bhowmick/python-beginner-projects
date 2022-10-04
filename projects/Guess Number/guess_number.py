import random


def guess_number(user_guess):
    num = random.randint(1, 50)
    while num != user_guess:
        if num < user_guess:
            print("Number is lower than " + str(user_guess))
            user_guess = int(input("Enter number between 1 to 50: "))
        elif num > user_guess:
            print("Number is higher than " + str(user_guess))
            user_guess = int(input("Enter number between 1 to 50: "))
        else:
            print()


user_guess = int(input("Enter number between 1 to 50: "))
guess_number(user_guess)
