from typing import List, Tuple
from abc import ABC, abstractmethod
import random

from utils import CollectionUtilsMixin, PrintMixin, PromptMixin
from player import Player
from board import Board


class Game(ABC):
    """Abstract base class for the Battleship game."""

    MAX_BOARD_SIZE = 15
    MIN_BOARD_SIZE = 5

    def __init__(self, board_size: int, player_1_name: str, player_2_name: str):
        """
        Initialize the game with the given parameters.

        Args:
            board_size (int): The size of the game board.
            player_1_name (str): Name of the first player.
            player_2_name (str): Name of the second player.

        To-Do for Implementer:
            - Initialize first player mover (i.e. self._current_player).
            - Implement place_ships() and use it to place the ships on the Board for each player.
            - Implement the game's main loop. This can be used for different UIs.
        """

        self.player_1: Player = Player(player_1_name, Board(board_size))
        self.player_2: Player = Player(player_2_name, Board(board_size))
        self.board_size: int = board_size

        self._current_player: Player | None = None

    @property
    def current_player(self) -> Player | None:
        """Gets the current player."""
        return self._current_player

    @current_player.setter
    def current_player(self, value):
        """Sets the current player."""
        self._current_player = value

    @property
    def previous_player(self) -> Player | None:
        """Gets the previous player."""
        return (
            self.player_1
            if self._current_player.name == self.player_2.name
            else self.player_2
        )

    def get_winner(self) -> Player | None:
        """
        Get the winner of the game.

        Returns:
            Player | None: The winning player or None if there is no winner yet.
        """
        if self.player_1.enemy_board.is_player_lost:
            return self.player_1
        elif self.player_2.enemy_board.is_player_lost:
            return self.player_2
        else:
            return None

    def update_player(self) -> None:
        """Update the current player to the next one."""
        self._current_player = (
            self.player_1
            if self._current_player.name == self.player_2.name
            else self.player_2
        )

    def make_current_player_attack(self, row: int, col: int) -> Player | None:
        """
        Make the current player's attack.

        Args:
            row (int): The row index of the attack.
            col (int): The column index of the attack.

        Returns:
            Player | None: The winning player or None if there is no winner yet.

        Raises:
            ValueError: If the first player to move was not initialized.
        """
        if self.current_player is None:
            raise ValueError("First Player to move was not initialized.")

        # Make Current Player Attack. Note that exceptions will be thrown from .attack() method
        self.current_player.attack(row, col)

        # Check if there is a Winner
        winner_or_none = self.get_winner()
        if winner_or_none is not None:
            return winner_or_none

        # Update the Current Player
        self.update_player()

    @abstractmethod
    def run(self, *args, **kwargs):
        """Abstract method to run the game."""
        pass

    @abstractmethod
    def place_ships(self, *args, **kwargs):
        """Abstract method to place ships on the board."""
        pass


class AlternatingGame(Game, CollectionUtilsMixin, PrintMixin):
    """
    Battleship Game with given alternative moves.

    Ad-hoc Setup
    ------------
    game = AlternatingGame(...)
    game.place_ships("<player_1>", [[(...), (...), ...], [(...), (...), ...], ...])
    game.place_ships("<player_2>", [[(...), (...), ...], [(...), (...), ...], ...])
    game.set_moves([(...), (...), ...], [(...), (...), ...])
    game.run(...)
    """

    PLAYER_1_MOVES = None
    PLAYER_2_MOVES = None

    def set_moves(
        self,
        player_1_moves: List[Tuple[int, int]],
        player_2_moves: List[Tuple[int, int]],
    ) -> None:
        """
        Set the moves for players.

        Args:
            player_1_moves (List[Tuple[int, int]]): List of moves for player 1.
            player_2_moves (List[Tuple[int, int]]): List of moves for player 2.

        Raises:
            ValueError: If the moves for players are already set.
        """
        if self.PLAYER_1_MOVES is not None or self.PLAYER_2_MOVES is not None:
            raise ValueError(
                f"The moves for {self.player_1.name} and {self.player_2.name} are already set."
            )

        # Check the validity of the given moves
        assert (
            len(player_1_moves) == self.board_size**2
        ), f"The number of moves must be {self.board_size ** 2}"
        assert (
            len(player_2_moves) == self.board_size**2
        ), f"The number of moves must be {self.board_size ** 2}"

        # Check for Duplicates and Out-of-Bound
        def all_cells_():
            return [
                (i, j) for i in range(self.board_size) for j in range(self.board_size)
            ]

        for player_moves in [player_1_moves, player_2_moves]:
            all_cells = all_cells_()
            for cell in player_moves:
                if cell not in all_cells:
                    raise ValueError(f"The cell {cell} is invalid.")
                all_cells.remove(cell)
            if len(all_cells) != 0:
                raise ValueError("There may be duplicates in the given moves.")

        self.PLAYER_1_MOVES = player_1_moves
        self.PLAYER_2_MOVES = player_2_moves

    def run(self, initial_player_name: str):
        """
        Run the alternating game.

        Args:
            initial_player_name (str): Name of the player who will make the first attack move.

        Raises:
            ValueError: If the given player does not belong to this game.
        """
        if initial_player_name not in [self.player_1.name, self.player_2.name]:
            raise ValueError(
                f'The given player "{initial_player_name}" does not belong to this Game.'
            )

        self.current_player = (
            self.player_1
            if initial_player_name == self.player_1.name
            else self.player_2
        )

        winner_or_none = self.get_winner()
        while winner_or_none is None:  # Stop the loop when there is a winner
            move = None
            if self.current_player == self.player_1:
                move = self.PLAYER_1_MOVES.pop(0)
            elif self.current_player == self.player_2:
                move = self.PLAYER_2_MOVES.pop(0)

            assert move is not None, "The move was not updated."

            self.make_current_player_attack(*move)
            winner_or_none = self.get_winner()

        print("Winner:", winner_or_none.name)

    def place_ships(
        self, player_name: str, ships_coordinates: List[List[Tuple[int, int]]]
    ) -> None:
        """
        Place ships on the board for the specified player.

        Args:
            player_name (str): The name of the player for whom the ships are to be placed.
            ships_coordinates (List[List[Tuple[int, int]]]): A list of ship coordinates to be placed on the board.

        Raises:
            ValueError: If the given player does not belong to this ConcreteGame.
        """
        if player_name not in [self.player_1.name, self.player_2.name]:
            raise ValueError("The given player does not belong to this ConcreteGame.")

        if player_name == self.player_1.name:
            for ship_coordinates in ships_coordinates:
                # Use player_2's enemy_board to place the ships for player_1
                self.player_2.place_ship(ship_coordinates)
        elif player_name == self.player_2.name:
            for ship_coordinates in ships_coordinates:
                # Use player_1's enemy_board to place the ships for player_2
                self.player_1.place_ship(ship_coordinates)


class CLIGame(Game, PrintMixin, PromptMixin):
    """
    CLI-based Battleship game.

    This class represents a Battleship game that is played in the command-line interface (CLI).
    It inherits from the `Game` class and includes methods for setting up the game, running the game loop,
    and placing ships on the board.

    Usage:
        game = CLIGame()
        game.run()
    """

    def __init__(self):
        board_size = self.prompt_board_size(
            f"Enter Board Size >>> ", "Invalid Board Size Input.\n"
        )
        player_1_name = self.prompt_name("Please Enter the Name for Player 1 >>> ")
        self.play_with_random_player = self.boolean_prompt(
            "Do you want to play with a bot? (yes/no) >>> "
        )
        player_2_name = self.prompt_name("Please Enter the Name for Player 2 >>> ")

        super().__init__(board_size, player_1_name, player_2_name)

        # Place the Ships Randomly
        print("Randomly placing ship ...")
        self.place_ships()

        # Select the First Mover Randomly
        self.current_player = random.choice([self.player_1, self.player_2])
        print(f"Player {self.current_player.name} moves first.")

    def run(self):
        """Start the game loop and handle player moves until a winner is determined."""

        while True:
            try:
                # Play with a Bot
                if (
                    self.play_with_random_player
                ):  # Assume that Player 2 is the Random Bot.
                    # Check if current player is player_2
                    if self.current_player == self.player_2:
                        # Make Random Valid Attack
                        valid_moves = [
                            move
                            for move in self.current_player.enemy_board.generate_valid_moves()
                        ]
                        attack_coordinate = random.choice(valid_moves)
                        print(
                            f"{self.player_2.name} (Bot) is attacking on {attack_coordinate} ...\n\n"
                        )
                        winner_or_none = self.make_current_player_attack(
                            *attack_coordinate
                        )

                    # Player 1's move
                    else:
                        attack_coordinate = self.attack_prompt(
                            self.board_size,
                            f"Please Enter the Attack Coordinates Admiral {self.current_player.name} >>> ",
                            "Invalid Attack Coordinate",
                        )
                        winner_or_none = self.make_current_player_attack(
                            *attack_coordinate
                        )

                        # Print Board State. When we make a move, it will automatically update for the next player
                        self.print_player_board(
                            self.previous_player, self.current_player
                        )
                else:
                    attack_coordinate = self.attack_prompt(
                        self.board_size,
                        f"Please Enter the Attack Coordinates Admiral {self.current_player.name} >>> ",
                        "Invalid Attack Coordinate",
                    )

                    winner_or_none = self.make_current_player_attack(*attack_coordinate)

                    # Print Board State. When we make a move, it will automatically update for the next player
                    self.print_player_board(self.previous_player, self.current_player)

                if winner_or_none is not None:
                    print(f"Player {winner_or_none.name} won the war!!!")
                    break
            except Exception as e:
                print(e)
                continue

    def place_ships(self):
        """Randomly place ships for both players."""
        self.player_1.generate_random_ship_arrangements()
        self.player_2.generate_random_ship_arrangements()


if __name__ == "__main__":
    cli_game = CLIGame()
    cli_game.run()
