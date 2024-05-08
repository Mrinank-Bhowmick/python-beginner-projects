from dataclasses import dataclass

from utils import generate_random_ships_arrangements
from board import Board


@dataclass
class Player:
    """
    Represents a player in the Battleship game.

    Attributes:
        name (str): The name of the player.
        enemy_board (Board): The board representing the opponent's board.
    """

    name: str
    enemy_board: Board

    def attack(self, row: int, col: int):
        """
        Attack a specific location on the opponent's board.

        Args:
            row (int): The row index of the target location.
            col (int): The column index of the target location.
        """
        self.enemy_board.enemy_move(row, col)

    def generate_random_ship_arrangements(self) -> None:
        """Generate random ship arrangements for the opponent's board and place them."""
        ships = generate_random_ships_arrangements(self.enemy_board.board_size)
        for ship in ships:
            self.enemy_board.place_ship(ship.coordinates)

    def place_ship(self, ship_coordinates):
        """
        Place a ship on the opponent's board.

        Args:
            ship_coordinates: Coordinates representing the ship's position.
        """
        # Remind that this is for the enemy's ships not this player.
        self.enemy_board.place_ship(ship_coordinates)
