import random

def roll_the_dice():
    # Set a variable for checking valid input
    valid_input = False

    # Loop asking the user for input as long as the input is invalid.
    while not valid_input:
        try:
            # Ask user for the type of they want!
            dice_type = int(input("Pick a Dice type: \n1. D4\n2. D6\n3. D8\n4. D10\n5. D12\n6. D20\n7. D100\n\n"))
            # Ask user how many dice they want to roll
            dice_amount = int(input("How many dice do you want to roll? (One or more.)\n\n"))

            # Check if the input is valid and setting the variable to True to stop a new loop from happening
            if dice_type not in range(1,8) or dice_amount <= 0:
                print("Invalid input! Choose a valid dice type and a valid amount of dice!")
            else:
                valid_input = True
                print("\nYou rolled:") 
        except ValueError:
            print("Invalid input. Choose a valid dice type and a valid amount of dice!")

        # Match the dice type with the input and print a random int for each of the dice the user wanted to roll
        match dice_type:
            case 1:
                for i in range(dice_amount):
                    number = random.randint(1, 4)
                    print(number)
                break
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
            # Added the extra text for the Nat 1 and Nat 20 for flavor!
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


# Calling the function
roll_the_dice()

