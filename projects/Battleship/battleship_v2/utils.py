from typing import List, Generator, Tuple
import random

from ship import Ship
from board import Board


def generate_row_ship_cells(
    board_size: int,
) -> Generator[List[Tuple[int, int]], None, None]:
    """
    Generator function to yield coordinates of ships aligned in rows.

    Args:
        board_size (int): The size of the game board.

    Yields:
        List[Tuple[int, int]]: List of tuples representing the coordinates of a ship aligned in a row.
    """
    for ship_size in range(1, board_size + 1):
        for i in range(board_size):  # Rows
            for j in range(board_size - ship_size + 1):  # Columns
                coordinates = [(i, col) for col in range(j, j + ship_size)]
                yield coordinates


def generate_column_ship_cells(board_size: int):
    """
    Generator function to yield coordinates of ships aligned in columns.

    Args:
        board_size (int): The size of the game board.

    Yields:
        List[Tuple[int, int]]: List of tuples representing the coordinates of a ship aligned in a column.
    """
    for ship_size in range(1, board_size + 1):
        for j in range(board_size):  # Columns
            for i in range(board_size - ship_size + 1):  # Rows
                coordinates = [(row, j) for row in range(i, i + ship_size)]
                yield coordinates


def generate_random_row_ship(board_size: int, ship_length: int) -> Ship:
    """
    Generates a random ship aligned in a row with the specified length.

    Args:
        board_size (int): The size of the game board.
        ship_length (int): The length of the ship.

    Returns:
        Ship: A Ship object representing the randomly generated ship aligned in a row.
    """
    row_ships = [
        Ship(cells)
        for cells in generate_row_ship_cells(board_size)
        if len(cells) == ship_length
    ]
    return random.choice(row_ships)


def generate_random_column_ship(board_size: int, ship_length: int) -> Ship:
    """
    Generates a random ship aligned in a column with the specified length.

    Args:
        board_size (int): The size of the game board.
        ship_length (int): The length of the ship.

    Returns:
        Ship: A Ship object representing the randomly generated ship aligned in a column.
    """
    column_ships = [
        Ship(cells)
        for cells in generate_column_ship_cells(board_size)
        if len(cells) == ship_length
    ]
    return random.choice(column_ships)


def generate_random_ships_arrangements(board_size: int) -> List[Ship]:
    """
    Generates a list of ships with random arrangements on the game board.

    Args:
        board_size (int): The size of the game board.

    Returns:
        List[Ship]: A list of Ship objects representing the randomly generated ships.
    """
    ships = []

    i = board_size
    while i > 0:
        row_or_col = random.choice(["row", "column"])
        if row_or_col == "row":
            ship = generate_random_row_ship(board_size, i)
        else:
            ship = generate_random_column_ship(board_size, i)

        if any(ship.is_ship_overlap(s) for s in ships):
            continue

        ships.append(ship)
        i -= 1

    n = len(ships)
    assert (n * (n + 1)) / 2 == len(
        [tup for ship in ships for tup in ship.coordinates]
    ), "Invalid Mathematical Assumption"

    return ships


class PromptMixin:
    """Mixin class providing static methods for prompting user input."""

    @staticmethod
    def prompt_board_size(
        prompt_message: str,
        error_message: str,
        min_board_size: int = 5,
        max_board_size: int = 15,
    ) -> int:
        """
        Prompt the user to input the size of the game board within specified bounds.

        Args:
            prompt_message (str): Message to prompt the user for input.
            error_message (str): Message to display in case of invalid input.
            min_board_size (int, optional): Minimum allowed board size. Defaults to 5.
            max_board_size (int, optional): Maximum allowed board size. Defaults to 15.

        Returns:
            int: Size of the game board input by the user.
        """

        while True:
            try:
                board_size = int(input(prompt_message))

                if board_size < min_board_size or board_size > max_board_size:
                    print(error_message)
                    continue

                return board_size

            except ValueError:
                print(error_message)
                continue

    @staticmethod
    def prompt_name(
        prompt_message: str, error_message: str = "Invalid Input! Please try again.\n"
    ) -> str:
        """
        Prompt the user to input a name.

        Args:
            prompt_message (str): Message to prompt the user for input.
            error_message (str, optional): Message to display in case of invalid input. Defaults to 'Invalid Input!
                Please try again.\n'.

        Returns:
            str: Name input by the user.
        """

        while True:
            input_name = input(prompt_message)

            # Check for invalid user input
            if input_name.strip() == "":
                print(error_message)
                continue

            return input_name

    @staticmethod
    def boolean_prompt(
        prompt_message: str,
        error_message: str = "Invalid Input! Please try again.\n",
        true_str: str = "yes",
        false_str: str = "no",
    ) -> bool:
        """
        Prompt the user to input a boolean value.

        Args:
            prompt_message (str): Message to prompt the user for input.
            error_message (str, optional): Message to display in case of invalid input.
                Defaults to 'Invalid Input! Please try again.\n'.
            true_str (str, optional): String representing a true value. Defaults to 'yes'.
            false_str (str, optional): String representing a false value. Defaults to 'no'.

        Returns:
            bool: Boolean value input by the user.
        """

        while True:
            bool_inp = input(prompt_message)

            # Check for Invalid User Input
            if bool_inp.lower() not in [true_str.lower(), false_str.lower()]:
                print(error_message)
                continue

            return bool_inp.lower() == true_str.lower()

    @staticmethod
    def attack_prompt(
        board_size: int,
        prompt_message: str,
        error_message: str = "Invalid Target! Pleas try again.",
    ) -> Tuple[int, ...]:
        """
        Prompt the user to input coordinates for an attack on the game board.

        Args:
            board_size (int): Size of the game board.
            prompt_message (str): Message to prompt the user for input.
            error_message (str, optional): Message to display in case of invalid input.
                Defaults to 'Invalid Target! Please try again.'.

        Returns:
            Tuple[int, ...]: Tuple containing the coordinates input by the user for the attack.
        """

        while True:
            attack_input = input(prompt_message)

            if len(attack_input.split()) != 2:
                print(error_message)
                continue

            try:
                attack_tuple = tuple(map(int, attack_input.split()))

                invalid_conditions = (
                    attack_tuple[0] < 0
                    or attack_tuple[0] >= board_size
                    or attack_tuple[1] < 0
                    or attack_tuple[1] >= board_size
                )

                if invalid_conditions:
                    print(
                        f"Attack Coordinates must be in [0, {board_size})\n"
                        + error_message
                    )
                    continue

                return attack_tuple
            except ValueError:
                print(error_message)
                continue


class PrintMixin:
    @staticmethod
    def print_player_board(player, other_player) -> None:
        """
        Print the current battlefield situation and targets for the specified player.

        Args:
            player (Player): The player whose perspective is being printed.
            other_player (Player): The opposing player.
        """

        player_board = other_player.enemy_board
        other_player_board = player.enemy_board

        player_board_state = player_board.get_board_for_player()
        player_hit_or_miss_state = other_player_board.get_board_for_enemy()

        print(f"{player.name} Battlefield Situation")
        Board.print_board(player_board_state)
        print()
        print(f"{player.name} Targets")
        Board.print_board(player_hit_or_miss_state)

        print("\n")


class CollectionUtilsMixin:
    """Mixin class providing static methods for manipulating collections."""

    @staticmethod
    def alternate_tuples(list1, list2):
        """
        Alternates the elements of two lists into a single list.

        Args:
            list1: First list.
            list2: Second list.

        Returns:
            List: Combined list with alternating elements from list1 and list2.
        """
        result = []
        max_len = max(len(list1), len(list2))

        for i in range(max_len):
            if i < len(list1):
                result.append(list1[i])
            if i < len(list2):
                result.append(list2[i])

        return result

    @staticmethod
    def shuffle(board_size) -> List[Tuple[int, int]]:
        """
        Shuffles the board cells for one player.

        Useful for generating random move sequence for one player.

        Args:
            board_size (int): Size of the game board.

        Returns:
            List[Tuple[int, int]]: Shuffled list of tuples representing board cells.
        """

        # Given the board size, generate random unique sequence of move for one player until all board
        # cells are generated.
        out_list = [(i, j) for i in range(board_size) for j in range(board_size)]
        random.shuffle(out_list)  # In-place modification for shuffle
        return out_list
