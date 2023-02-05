import random


def guess(x):
    n = random.randrange(1, 10)
    guess = int(input("Enter any number: "))
    while n != guess:
        if guess < n:
            print("OOPS! Too low")
            guess = int(input("Guess again: "))
        elif guess > n:
            print("OOPS! Too high!")
            guess = int(input("Guess again: "))
        else:
            break
    print(f"Congratulations!! You guess the number {n} correctly")


def computer_guess():
    x = int(input("Enter your number: "))
    low = 1
    high = x
    CompAns = ""
    while CompAns != "c":
        if low != high:
            CompGuess = random.randint(low, high)
        else:
            CompGuess = low
        CompAns = input(
            f"Is {CompGuess} too high (h), too low (l), or correct (c)? \n=>"
        ).lower()
        if CompAns == "h":
            high = CompGuess - 1
        elif CompAns == "l":
            low = CompGuess + 1

    print(f"Yay! The computer guessed your number, {CompGuess}, correctly!")


if __name__ == "__main__":
    print(
        "Select gaming mode\n Press 1 to guess the number\nPress 2 to choose the number"
    )
    Gmode = int(input())
    if Gmode == 1:
        guess(10)
    if Gmode == 2:
        computer_guess()
