"""
snake water gun
10 times play using while

Snake water gun

Snake Water Gun Game in Python
The snake drinks the water, the gun shoots the snake, and gun has no effect on water.

NOTE: Install rich before playing this game by the command "pip install rich".
"""

import random
from rich import print as rprint

if __name__ == "__main__":
    CHOICES = ["s", "w", "g"]

    CHANCE = 10
    NO_OF_CHANCE = 0
    COMPUTER_POINT = 0
    HUMAN_POINT = 0

    print(" \t \t \t \t Snake,Water,Gun Game\n \n")
    rprint(
        "[yellow]s[/yellow] for snake, [blue]w[/blue] for water, [green]g[/green] for gun \n"
    )

    # making the game in while
    while NO_OF_CHANCE < CHANCE:
        user_choice = input("Enter your choice >> ")
        computer_choice = random.choice(CHOICES)

        if user_choice.lower() not in CHOICES:
            rprint("[red]Wrong input!![/red] \n")
        elif user_choice == computer_choice:
            rprint("Tie!! 0 point to each \n ")
        else:
            if user_choice.lower() == "s":
                if computer_choice == "g":
                    COMPUTER_POINT += 1
                    WINNER = "Computer"
                elif computer_choice == "w":
                    HUMAN_POINT += 1
                    WINNER = "Human"
            elif user_choice.lower() == "w":
                if computer_choice == "s":
                    COMPUTER_POINT += 1
                    WINNER = "Computer"
                elif computer_choice == "g":
                    HUMAN_POINT += 1
                    WINNER = "Human"
            elif user_choice.lower() == "g":
                if computer_choice == "s":
                    HUMAN_POINT += 1
                    WINNER = "Human"
                elif computer_choice == "w":
                    COMPUTER_POINT += 1
                    WINNER = "Computer"
            rprint(
                f"You guessed [yellow]{user_choice.lower()}[/yellow] and Computer guessed [cyan]{computer_choice}.[/cyan]\n"
            )
            rprint(
                f"[{'green' if WINNER == 'Human' else 'red'}]{WINNER} wins 1 point[/{'green' if WINNER == 'Human' else 'red'}] \n"
            )

        NO_OF_CHANCE += 1
        rprint(f"{CHANCE - NO_OF_CHANCE} chance(s) are left out of {CHANCE} chances.\n")

    print("Game over!")

    if COMPUTER_POINT == HUMAN_POINT:
        rprint("[yellow]Tie![/yellow]")

    elif COMPUTER_POINT > HUMAN_POINT:
        rprint("[red]Computer won and you lost.[/red]")

    else:
        rprint("[green]You won and Computer lost.[/green]")

    rprint(
        f"[green]Your points: {HUMAN_POINT}\tComputer points: {COMPUTER_POINT}[/green]"
    )
