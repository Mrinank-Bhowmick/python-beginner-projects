import random
from rich import print as rprint


def get_computer_choice(choices: list[str]) -> str:
    """
    Randomly selects a choice for the computer from the given options.
    """
    return random.choice(choices)


def determine_winner(user_choice: str, computer_choice: str) -> tuple[str, int]:
    """
    Determines the winner of the current round.
    Returns a tuple of winner ('Human', 'Computer', or 'Tie') and the points earned (1 or 0).
    """
    if user_choice == computer_choice:
        return "Tie", 0

    winning_combinations = {
        "s": "w",  # Snake drinks water
        "w": "g",  # Water extinguishes gun
        "g": "s",  # Gun shoots snake
    }

    if winning_combinations[user_choice] == computer_choice:
        return "Human", 1
    else:
        return "Computer", 1


def display_score(chances_left: int, total_chances: int, human_points: int, computer_points: int) -> None:
    """
    Displays the current score and remaining chances.
    """
    rprint(f"[yellow]{chances_left} chance(s) left out of {total_chances}.[/yellow]")
    rprint(f"[green]Your points: {human_points}[/green]")
    rprint(f"[red]Computer points: {computer_points}[/red]\n")


def snake_water_gun_game() -> None:
    """
    Main function to play the Snake Water Gun game.
    """
    CHOICES = ["s", "w", "g"]
    CHANCES = 10

    human_points = 0
    computer_points = 0

    print("\t" * 4 + "Snake, Water, Gun Game\n")
    rprint("[yellow]s[/yellow] for snake, [blue]w[/blue] for water, [green]g[/green]\n")

    for chance in range(1, CHANCES + 1):
        user_choice = input("Enter your choice >> ").lower()

        if user_choice not in CHOICES:
            rprint("[red]Invalid input! Please choose 's', 'w', or 'g'.[/red]\n")
            continue

        computer_choice = get_computer_choice(CHOICES)
        winner, points = determine_winner(user_choice, computer_choice)

        if winner == "Human":
            human_points += points
        elif winner == "Computer":
            computer_points += points

        rprint(
            f"You chose [yellow]{user_choice}[/yellow], Computer chose [cyan]{computer_choice}[/cyan].\n"
        )
        rprint(
            f"[{'green' if winner == 'Human' else 'red'}]{winner} wins this round![/{'green' if winner == 'Human' else 'red'}]\n"
        )
        display_score(CHANCES - chance, CHANCES, human_points, computer_points)

    rprint("[bold magenta]Game over![/bold magenta]\n")

    if human_points > computer_points:
        rprint("[green]Congratulations! You won the game![/green]")
    elif human_points < computer_points:
        rprint("[red]Computer wins! Better luck next time.[/red]")
    else:
        rprint("[yellow]It's a tie![/yellow]")

    rprint(
        f"[green]Final Score:[/green] [blue]You: {human_points}, Computer: {computer_points}[/blue]"
    )


if __name__ == "__main__":
    snake_water_gun_game()
