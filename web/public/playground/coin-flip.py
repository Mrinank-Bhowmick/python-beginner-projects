# === Coin Flip · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @pranavdasan.

import random


# Randomly return "heads" or "tails"
def toss_coin():
    list1 = ["heads", "tails"]
    return random.choice(list1)


# Run the coin flip game loop
def main():
    while True:
        flag = False

        # Ask player to pick heads or tails
        answer = input("Pick a side for the coin toss (heads/tails): ")

        # Restart loop if input is invalid
        if answer.lower() not in ["heads", "tails"]:
            continue

        # Flip the coin and show the result
        result = toss_coin()

        print(f"You got... {result}")

        if answer.lower() == result:
            print("Nice, you won the coin toss!!")
        else:
            print("OOF. Better luck next time.")

        # Ask if the player wants to play again
        while True:
            answer_y = input("Wanna play again? (yes/no): ")
            if answer_y.lower() == "no" or answer_y.lower() == "n":
                flag = True
                break
            elif answer_y.lower() == "yes" or answer_y.lower() == "y":
                break
            else:
                continue

        # Exit the outer loop if done
        if flag:
            break


if __name__ == "__main__":
    main()
