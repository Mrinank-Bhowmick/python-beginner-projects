from random import randint

print("Welcome to the Higher-Lower Game!")
rnum = randint(0, 100)
noguesses = 0
while True:

    while True:
        guess = input("Guess the number: ")
        if guess.isdigit():
            # Check if the input string consists of digits only
            integer_number = int(guess)
            print("You entered:", integer_number)

            if integer_number > rnum:
                print("Lower")
            elif integer_number < rnum:
                print("Higher")
            else:
                (print("You win! the number is " + guess + "!"), quit())
            noguesses += 1
        else:
            print("Invalid input. Please enter an integer number.")
