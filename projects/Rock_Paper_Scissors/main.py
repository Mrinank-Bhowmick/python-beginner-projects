from random import randint


def main():
    choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
    score = 0
    attempts = 0

    while True:
        your_choice = int(input("\n1. Rock, 2. Paper, 3. Scissors, 4. Exit: "))

        if your_choice == 4:
            break
        if your_choice not in {1, 2, 3}:
            print("Invalid choice.")
            break

        computer_choice = randint(1, 3)
        attempts += 1
        print(
            f"You chose {choices[your_choice]} and computer chose {choices[computer_choice]}")

        if your_choice == computer_choice:
            print("Its a draw.")
            attempts -= 1
        elif str(your_choice)+str(computer_choice) in ["13", "21", "32"]:
            print("You Win!")
            score += 1
        else:
            print("You Lose.")

    print(f"Your score is {score}/{attempts}")
    print("Thanks for playing.")


main()
