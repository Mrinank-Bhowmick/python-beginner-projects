import random

# Ask user for the type of they want!
dice_type = int(input("Pick a Dice type: \n1. D4\n2. D6\n3. D8\n4. D10\n5. D12\n6. D20\n7. D100\n\n"))

# use switch cases introduced in Python 3.10
match dice_type:
    case 1:
        number = random.randint(1, 4)
        print(number)
    case 2:
        number = random.randint(1, 6)
        print(number)
    case 3:
        number = random.randint(1, 8)
        print(number)
    case 4:
        number = random.randint(1, 10)
        print(number)
    case 5:
        number = random.randint(1, 12)
        print(number)
    case 6:
        number = random.randint(1, 20)
        print(number)
    case 7:
        number = random.randint(1, 100)
        print(number)
    case _:
        print("Not a valid option, Adios <3")
        exit()
