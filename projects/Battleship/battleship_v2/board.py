from typing import List, Tuple, Generator
from dataclasses import dataclass

from exceptions import BoardException
from ship import Ship


@dataclass
class BoardStatesPlayerPOV:
    """Cell's State Labels from Player's Point-of-View."""

    missed: str = "M"
    hit: str = "H"
    ship: str = "S"
    unoccupied: str = "-"


@dataclass
class BoardStatesEnemyPOV:
    """Cell's State Labels from Enemy's Point-of-View."""

    hit: str = "X"
    missed: str = "O"
    no_move: str = "-"


class Board:
    """Represents the Battleship Board."""

    def __init__(self, board_size: int, empty_label=" "):
        """
        Initializes the Board object.

        Args:
            board_size (int): The size of the game board.
            empty_label (str, optional): Label representing empty cells on the board. Defaults to " ".

        Raises:
            BoardException: If an invalid board size is given.
        """

        if board_size < 5 or board_size > 15:
            raise BoardException(
                "Invalid given board size. Board size must be 5 to 15."
            )

        self.board_size = board_size
        self._empty_label = empty_label

        self._board = [
            [self._empty_label for _ in range(self.board_size)]
            for _ in range(self.board_size)
        ]

        # Instantiate Labels for Player and Enemy POVs
        self._player_pov_labels = BoardStatesPlayerPOV()
        self._enemy_pov_labels = BoardStatesEnemyPOV()

        self.ships: List[Ship] = []  # List of Ships

        # Keep track of all enemy actions/moves for "Missed" and "No Move".
        # Hit can be obtained from `hit_cells` property.
        self._enemy_moves = {"hit": [], "missed": []}

    @property
    def num_of_ships(self):
        """Returns the number of ships on the board."""
        return len(self.ships)

    @property
    def dead_ships(self) -> List[Ship]:
        """Returns a list of destroyed ships."""
        return [ship for ship in self.ships if ship.is_destroyed]

    @property
    def hit_cells(self) -> List[Tuple[int, int]]:
        """Returns a list of coordinates of cells hit by enemy."""
        return [cell for ship in self.ships for cell in ship.hit_cells]

    @property
    def un_hit_cells(self) -> List[Tuple[int, int]]:
        """Returns a list of coordinates of un-hit cells."""
        return [cell for ship in self.ships for cell in ship.un_hit_cells]

    @property
    def occupied_cells(self) -> List[Tuple[int, int]]:
        """Returns a list of coordinates of cells occupied by ships."""
        return [cell for ship in self.ships for cell in ship.coordinates]

    @property
    def is_player_lost(self) -> bool:
        """Returns True if all player's ships are destroyed, otherwise False."""
        return all(ship.is_destroyed for ship in self.ships)

    @property
    def valid_moves(self) -> List[Tuple[int, int]]:
        """Returns a list of available valid moves."""
        all_cells_generator = (
            (i, j) for i in range(self.board_size) for j in range(self.board_size)
        )
        return [
            cell
            for cell in all_cells_generator
            if cell not in self._enemy_moves["hit"] + self._enemy_moves["missed"]
        ]

    def generate_valid_moves(self) -> Generator[Tuple[int, int], None, None]:
        """Yields all the available valid moves."""
        board = self.get_board_for_enemy()
        for i in range(self.board_size):
            for j in range(self.board_size):
                if board[i][j] == self._enemy_pov_labels.no_move:
                    # yield board[i][j]
                    yield i, j

    def get_board_for_player(self) -> List[List[str]]:
        """Gets the Board States from Player's POV."""
        # Initialize an empty board.
        board = self._create_empty_board()

        # Fill with Ships' Positions
        for ship in self.ships:
            for row, col in ship.coordinates:
                board[row][col] = self._player_pov_labels.ship

        # Fill with Hit
        for row, col in self._enemy_moves["hit"]:
            board[row][col] = self._player_pov_labels.hit

        # Fill with Missed
        for row, col in self._enemy_moves["missed"]:
            board[row][col] = self._player_pov_labels.missed

        # Fill with Unoccupied
        for row in range(self.board_size):
            for col in range(self.board_size):
                if board[row][col] == self._empty_label:
                    board[row][col] = self._player_pov_labels.unoccupied

        return board

    def get_board_for_enemy(self) -> List[List[str]]:
        """Gets the Board States from Enemy's POV."""
        # Initialize an empty board.
        board = self._create_empty_board()

        # Fill with Hit
        for row, col in self._enemy_moves["hit"]:
            board[row][col] = self._enemy_pov_labels.hit

        # Fill with Missed
        for row, col in self._enemy_moves["missed"]:
            board[row][col] = self._enemy_pov_labels.missed

        # Fill with No Moves
        for row in range(self.board_size):
            for col in range(self.board_size):
                if board[row][col] == self._empty_label:
                    board[row][col] = self._enemy_pov_labels.no_move

        return board

    def _create_empty_board(self) -> List[List[str]]:
        """Creates an empty board."""
        return [
            [self._empty_label for _ in range(self.board_size)]
            for _ in range(self.board_size)
        ]

    @staticmethod
    def print_board(board: List[List[str]]) -> None:
        """Prints a game board and it's states."""
        board_size = len(board)
        # Print the Column Numbers for first row (0 to board_size - 1)
        print(f" ", end="")  # Print the Initial Spaces
        for col in range(board_size):
            if col > 9:
                print(f"  {col}", end="")  # For 0 to 9
            else:
                print(f"   {col}", end="")  # For 10 to 14
        print()  # new line

        for row in range(board_size):
            if row > 9:
                print(f"{row} ", end="")
            else:
                print(f" {row} ", end="")
            for col in range(board_size):
                if col > 9:
                    print(f" {board[row][col]}", end="")
                else:
                    print(f" {board[row][col]} ", end="")

                if col < board_size - 1:
                    if col > 9:
                        print(" |", end="")  # Separate cells with |
                    else:
                        print("|", end="")  # Separate cells with |
            print()  # Move to the next line after printing the row

    def place_ship(self, coordinates: List[Tuple[int, int]]) -> None:
        """Places a ship on the board."""
        # Check if player can still place a ship based on the board & ship size constraints.
        if self.num_of_ships > self.board_size:
            raise BoardException("Cannot place another ship on the board.")

        # Check if there's an invalid cell/coordinate to place a ship.
        for row, col in coordinates:
            if row < 0 or row >= self.board_size or col < 0 or col >= self.board_size:
                raise BoardException(f"Invalid cell to place a ship: ({row}, {col})")

        # Check if a cell is already occupied.
        if not all(not self._is_cell_occupied(*cell) for cell in coordinates):
            raise BoardException("Some of the given cells are already occupied.")

        # Create a New Ship
        new_ship = Ship(coordinates)

        # Add the ship to the list
        self.ships.append(new_ship)

    def _is_cell_occupied(self, row: int, col: int) -> bool:
        """Returns True if a cell is occupied by another ship, otherwise False."""
        return any((row, col) in ship.coordinates for ship in self.ships)

    def which_ship(self, row: int, col: int) -> None | Ship:
        """Returns the Ship that occupies the cell. Otherwise, None."""
        for ship in self.ships:
            if (row, col) in ship.coordinates:
                return ship
        return None

    def enemy_move(self, row: int, col: int) -> None:
        """Performs an enemy's move."""

        # Check if the coordinate is already a hit or missed.
        board = self.get_board_for_enemy()
        if board[row][col] in [
            self._enemy_pov_labels.hit,
            self._enemy_pov_labels.missed,
        ]:
            raise BoardException(
                f"The given coordinate ({row}, {col}) already has {board[row][col]}."
            )

        ship: None | Ship = self.which_ship(row, col)

        if isinstance(ship, Ship):
            # Update states in the ship
            ship.hit_ship(row, col)
            self._enemy_moves["hit"].append((row, col))
        else:
            self._enemy_moves["missed"].append((row, col))
