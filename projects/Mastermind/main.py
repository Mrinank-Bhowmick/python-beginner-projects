import random

num = random.randrange(1000, 10000)

n = int(input("Guess the 4 digit number:"))

# guess made. Program terminates if true.
if n == num:
    print("Great! You guessed the number in just 1 try! You're a Mastermind!")
else:
    # ctr variable initialized. It will keep count of
    # the number of tries the Player takes to guess the number.
    ctr = 0

    # while loop repeats as long as the
    # Player fails to guess the number correctly.
    while n != num:
        # variable increments every time the loop
        # is executed, giving an idea of how many
        # guesses were made.
        ctr += 1

        count = 0

        # explicit type conversion of an integer to
        # a string in order to ease extraction of digits
        n = str(n)

        # explicit type conversion of a string to an integer
        num = str(num)

        # correct[] list stores digits which are correct
        correct = ["X"] * 4

        # for loop runs 4 times since the number has 4 digits.
        for i in range(0, 4):
            # checking for equality of digits
            if n[i] == num[i]:
                # number of digits guessed correctly increments
                count += 1
                # hence, the digit is stored in correct[].
                correct[i] = n[i]
            else:
                continue

        # when not all the digits are guessed correctly.
        if (count < 4) and (count != 0):
            print("Not quite the number. But you did get ", count, " digit(s) correct!")
            print("Also these numbers in your input were correct.")
            for k in correct:
                print(k, end=" ")
            print("\n")
            print("\n")
            n = int(input("Enter your next choice of numbers: "))

        # when none of the digits are guessed correctly.
        elif count == 0:
            print("None of the numbers in your input match.")
            n = int(input("Enter your next choice of numbers: "))

    # condition for equality.
    if n == num:
        print("You've become a Mastermind!")
        print("It took you only", ctr, "tries.")
