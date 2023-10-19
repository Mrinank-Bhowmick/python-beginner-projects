import random

def roll_the_dice():
    valid_dice = (4, 6, 8, 10, 12, 20, 100)
    # Ask user for the type of they want!
    dice_type = int(input("Pick a Dice type: \n1. D4\n2. D6\n3. D8\n4. D10\n5. D12\n6. D20\n7. D100\n\n"))
    dice_amount = int(input("How many dice do you want to roll? (One or more.)\n\n"))
    try: 
        match dice_type:
            case 1:
                for i in range(dice_amount):
                    number = random.randint(1, 4)
                    print(number)
            case 2:
                for i in range(dice_amount):
                    number = random.randint(1, 6)
                    print(number)
            case 3:
                for i in range(dice_amount):
                    number = random.randint(1, 8)
                    print(number)
            case 4:
                for i in range(dice_amount):
                    number = random.randint(1, 10)
                    print(number)
            case 5:
                for i in range(dice_amount):
                    number = random.randint(1, 12)
                    print(number)
            case 6:
               for i in range(dice_amount):
                    number = random.randint(1, 20)
                    if number == 1:
                        print("Natural 1!")
                    elif number == 20:
                        print("Natural 20!")
                    else:
                        print(number)
            case 7:
                for i in range(dice_amount):
                    number = random.randint(1, 100)
                    print(number)
            case _:
                print("Not a valid option!")
                exit()

    except ValueError:
        print("Invalid input. Choose a valid dice type and a valid amount of dice!")




roll_the_dice()

