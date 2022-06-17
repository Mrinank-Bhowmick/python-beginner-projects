from random import randint

rnum = randint(0, 100)
noguesses = 0
while True:
    guess = int(input(": "))
    if guess > rnum:
        print("Lower")
    elif guess < rnum:
        print("Higher")
    else:
        (print("You win ({noguesses} guesses used)"), quit())
    noguesses += 1
