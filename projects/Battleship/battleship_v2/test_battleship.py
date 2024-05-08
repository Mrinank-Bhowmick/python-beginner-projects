import unittest

from utils import *
from exceptions import *
from player import Player
from board import Board
from game import Game


class TestShip(unittest.TestCase):
    """Test cases for the Ship class."""

    def test_valid_ship_instantiation(self):
        """Test valid ship instantiation for both row and column ships."""

        for cells in generate_row_ship_cells(5):
            ship = Ship(cells)
            self.assertFalse(ship.is_destroyed)
            self.assertEqual(ship.num_hits, 0)

        for cells in generate_column_ship_cells(5):
            ship = Ship(cells)
            self.assertFalse(ship.is_destroyed)
            self.assertEqual(ship.num_hits, 0)

    def test_invalid_ship_instantiation(self):
        """Test invalid ship instantiation with various arguments."""

        ship_args = [
            [],
            [(-1, 2), (51, 2), (2, 2)],
            [(0, 2), (1, -12), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
            [(0, 2), (1, 2), (2, 2), (1, 2)],
        ]

        for ship_arg in ship_args:
            with self.assertRaises(InvalidShipCoordinateException):
                Ship(ship_arg)

        ship_args = [[(0, 2), (1, 2), (4, 2)], [(1, 0), (1, 2), (1, 3)]]

        for ship_arg in ship_args:
            with self.assertRaises(AssertionError):
                Ship(ship_arg)

    def test_ship_damaged_but_not_destroyed(self):
        """Test ship instance when it's damaged but not destroyed."""

        ship = Ship([(0, 2), (1, 2), (2, 2)])
        ship.hit_ship(0, 2)
        ship.hit_ship(1, 2)

        self.assertEqual(ship.num_hits, 2)
        self.assertEqual(len(ship.un_hit_cells), 1)
        self.assertFalse(ship.is_destroyed)

    def test_ship_destroyed(self):
        """Test ship instance when it's destroyed."""

        ship = Ship([(0, 2), (1, 2), (2, 2)])
        ship.hit_ship(0, 2)
        ship.hit_ship(1, 2)
        ship.hit_ship(2, 2)

        self.assertEqual(ship.num_hits, 3)
        self.assertEqual(len(ship.un_hit_cells), 0)
        self.assertTrue(ship.is_destroyed)

    def test_no_ship_overlap(self):
        """Test when there is no overlap between two ships."""

        ship1 = Ship([(0, 2), (1, 2), (2, 2)])
        ship2 = Ship([(2, 0), (2, 1)])

        result = ship1.is_ship_overlap(ship2)
        self.assertFalse(result)

    def test_ships_overlap(self):
        """Test when two ships overlap."""

        ship1 = Ship([(0, 2), (1, 2), (2, 2)])
        ship2 = Ship([(2, 0), (2, 1), (2, 2)])

        result = ship1.is_ship_overlap(ship2)
        self.assertTrue(result)


class TestBoard(unittest.TestCase):
    """Test cases for the Board class."""

    def setUp(self):
        """Set up with a predefined board and ship positions."""

        self.board = Board(5)

        # Player's POV Board
        # S | S | S | S | S |
        # S | S | - | S | S |
        # - | - | - | S | S |
        # S | - | - | S | S |
        # - | - | - | S | - |

        # Enemy's POV Board
        # - | - | - | - | - |
        # - | - | - | - | - |
        # - | - | - | - | - |
        # - | - | - | - | - |
        # - | - | - | - | - |

        self.ships_positions = [
            [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
            [(1, 3), (2, 3), (3, 3), (4, 3)],
            [(1, 4), (2, 4), (3, 4)],
            [(1, 0), (1, 1)],
            [(3, 0)],
        ]

    def add_ships_to_board(self):
        """Add ships to the board based on predefined ship positions."""

        for position in self.ships_positions:
            self.board.place_ship(position)

    def print_boards(self):
        """Print the player's and enemy's POV boards."""

        board = self.board.get_board_for_player()
        print("Player's POV Board")
        Board.print_board(board)
        print("\nEnemy's POV Board")
        board = self.board.get_board_for_enemy()
        Board.print_board(board)

    def test_place_ships(self):
        """Test placing ships on the board."""

        self.add_ships_to_board()
        self.assertEqual(len(self.board.occupied_cells), 15)

    def test_place_ship_on_occupied_cell(self):
        """Test placing a ship on an already occupied cell."""

        self.board.place_ship([(0, 0), (0, 1)])
        with self.assertRaises(BoardException):
            self.board.place_ship([(0, 0), (1, 0)])

    def test_place_ship_with_invalid_cell(self):
        """Test placing a ship with invalid cell coordinates."""

        with self.assertRaises(BoardException):
            self.board.place_ship([(6, 0), (5, 0)])

    def test_enemy_move_hit(self):
        """Test enemy's move resulting in a hit."""

        self.add_ships_to_board()

        self.board.enemy_move(0, 0)
        self.board.enemy_move(3, 0)

        self.assertEqual(len(self.board.dead_ships), 1)
        self.assertEqual(len(self.board.hit_cells), 2)
        self.assertEqual(len(self.board.un_hit_cells), 13)
        self.assertFalse(self.board.is_player_lost)
        self.assertEqual(len(self.board.valid_moves), 23)

    def test_enemy_move_missed(self):
        """Test enemy's move resulting in a miss."""

        self.add_ships_to_board()

        self.board.enemy_move(1, 2)
        self.board.enemy_move(4, 4)

        self.assertEqual(len(self.board.dead_ships), 0)
        self.assertEqual(len(self.board.hit_cells), 0)
        self.assertEqual(len(self.board.un_hit_cells), 15)
        self.assertFalse(self.board.is_player_lost)
        self.assertEqual(len(self.board.valid_moves), 23)

    def test_player_lost(self):
        """Test scenario where player loses the game."""

        self.board.place_ship([(1, 4), (2, 4), (3, 4)])
        self.board.place_ship([(1, 0), (1, 1)])

        # print("Before")
        # self.print_boards()

        attack_moves = [(1, 4), (2, 4), (3, 4), (1, 0), (1, 1)]

        for attack_move in attack_moves:
            self.board.enemy_move(*attack_move)

        # print("\n\nAfter")
        # self.print_boards()

        self.assertEqual(len(self.board.dead_ships), 2)
        self.assertEqual(len(self.board.hit_cells), 5)
        self.assertEqual(len(self.board.un_hit_cells), 0)
        self.assertTrue(self.board.is_player_lost)
        self.assertEqual(len(self.board.valid_moves), 20)


class ConcreteGame(Game):
    """A concrete implementation of the Game abstract class."""

    def init(self):
        """Initialize the game by setting the initial player."""
        # Let Player 1 to be the Initial Mover
        self.current_player = self.player_1

    def run(self, row, col):
        """Run the game by making the current player's attack at the specified row and column."""
        winner_or_none = self.make_current_player_attack(row, col)

    def place_ships(self, player_name: str, ships_coordinates: list):
        """
        Place ships for the specified player.

        Args:
            player_name (str): The name of the player.
            ships_coordinates (list): List of ship coordinates to be placed on the board.

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


class TestGame(unittest.TestCase):
    """Test cases for the Game class."""

    def setUp(self):
        """
        Player 1 - Ships and their Arrangement (board_size=5)
        [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)]
        [(3, 1), (3, 2), (3, 3), (3, 4)]
        [(4, 2), (4, 3), (4, 4)]
        [(0, 2), (1, 2)]
        [(3, 0)]

        Player 2 - Ships and their Arrangement (board_size=5)
        [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)]
        [(0, 1), (1, 1), (2, 1), (3, 1)]
        [(2, 3), (3, 3), (4, 3)]
        [(3, 4), (4, 4)]
        [(3, 0)]
        """
        board_size = 5
        player_1_name = "Player 1"
        player_2_name = "Player 2"
        self.concrete_game = ConcreteGame(board_size, player_1_name, player_2_name)

        # Initialize to set current_player to be player_1
        self.concrete_game.init()

        # Place the Ships for Player 1 and Player 2
        self._setup_place_ships()

        # Set the Players' Moves
        self._set_player_moves()

    def _setup_place_ships(self):
        """Helper method to place ships for both players."""

        # Player 1
        ships = [
            [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
            [(3, 1), (3, 2), (3, 3), (3, 4)],
            [(4, 2), (4, 3), (4, 4)],
            [(0, 2), (1, 2)],
            [(3, 0)],
        ]
        self.concrete_game.place_ships(self.concrete_game.player_1.name, ships)

        # Player 2
        ships = [
            [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
            [(0, 1), (1, 1), (2, 1), (3, 1)],
            [(2, 3), (3, 3), (4, 3)],
            [(3, 4), (4, 4)],
            [(3, 0)],
        ]
        self.concrete_game.place_ships(self.concrete_game.player_2.name, ships)

    def _set_player_moves(self):
        """Set player moves."""

        # Constants - Separate Moves
        # Assumption: Player 1 Moves First
        # Player 1 Wins
        self.PLAYER_1_WINS_PLAYER_1_MOVES = [
            (3, 1),
            (0, 1),
            (0, 0),
            (4, 0),
            (1, 1),
            (0, 3),
            (3, 0),
            (1, 0),
            (1, 2),
            (4, 3),
            (3, 2),
            (1, 4),
            (0, 4),
            (2, 4),
            (1, 3),
            (4, 2),
            (3, 3),
            (0, 2),
            (2, 2),
            (3, 4),
            (2, 1),
            (4, 4),
            (2, 3),
            (4, 1),
            (2, 0),
        ]
        self.PLAYER_1_WINS_PLAYER_2_MOVES = [
            (0, 4),
            (0, 2),
            (3, 4),
            (1, 0),
            (4, 0),
            (1, 3),
            (2, 1),
            (1, 2),
            (2, 0),
            (2, 3),
            (3, 1),
            (0, 3),
            (2, 4),
            (0, 0),
            (1, 4),
            (2, 2),
            (0, 1),
            (1, 1),
            (3, 3),
            (4, 3),
            (3, 2),
            (3, 0),
            (4, 1),
            (4, 4),
            (4, 2),
        ]

        # Player 2 Wins
        self.PLAYER_2_WINS_PLAYER_1_MOVES = [
            (1, 3),
            (2, 1),
            (2, 2),
            (2, 3),
            (0, 4),
            (4, 3),
            (3, 0),
            (0, 3),
            (1, 0),
            (0, 0),
            (2, 0),
            (0, 2),
            (4, 2),
            (3, 3),
            (1, 2),
            (1, 1),
            (4, 0),
            (4, 4),
            (2, 4),
            (0, 1),
            (3, 2),
            (4, 1),
            (3, 1),
            (1, 4),
            (3, 4),
        ]
        self.PLAYER_2_WINS_PLAYER_2_MOVES = [
            (3, 1),
            (1, 3),
            (0, 4),
            (2, 0),
            (2, 3),
            (2, 2),
            (3, 2),
            (4, 3),
            (3, 3),
            (0, 2),
            (4, 2),
            (1, 1),
            (4, 4),
            (4, 1),
            (0, 0),
            (3, 0),
            (0, 1),
            (0, 3),
            (1, 2),
            (2, 1),
            (3, 4),
            (2, 4),
            (1, 0),
            (1, 4),
            (4, 0),
        ]

    def test_game_initialization(self):
        """Test game initialization."""

        # UtilsMixin.alternate_tuples()
        self.assertEqual(self.concrete_game.player_1.name, "Player 1")
        self.assertEqual(self.concrete_game.player_2.name, "Player 2")

        self.assertEqual(self.concrete_game.board_size, 5)
        self.assertEqual(self.concrete_game.current_player, self.concrete_game.player_1)
        self.assertNotEqual(
            self.concrete_game.current_player, self.concrete_game.player_2
        )
        self.assertIsNone(self.concrete_game.get_winner())

        # Test Ship Arrangement is correct for Player 1
        ships = [
            [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
            [(3, 1), (3, 2), (3, 3), (3, 4)],
            [(4, 2), (4, 3), (4, 4)],
            [(0, 2), (1, 2)],
            [(3, 0)],
        ]
        player_1_occupied_cells = self.concrete_game.player_2.enemy_board.occupied_cells
        for cell in (tup for ship_coordinates in ships for tup in ship_coordinates):
            self.assertIn(cell, player_1_occupied_cells)

        # Test Ship Arrangement is correct for Player 2
        ships = [
            [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
            [(0, 1), (1, 1), (2, 1), (3, 1)],
            [(2, 3), (3, 3), (4, 3)],
            [(3, 4), (4, 4)],
            [(3, 0)],
        ]
        player_2_occupied_cells = self.concrete_game.player_1.enemy_board.occupied_cells
        for cell in (tup for ship_coordinates in ships for tup in ship_coordinates):
            self.assertIn(cell, player_2_occupied_cells)

    def test_current_player_updating(self):
        """Test whether the current player is updated correctly after each move."""

        self.assertEqual(
            self.concrete_game.previous_player, self.concrete_game.player_2
        )
        self.assertEqual(self.concrete_game.current_player, self.concrete_game.player_1)

        # Player 1's Move (State Transition from Player 1 to 2)
        self.concrete_game.make_current_player_attack(0, 0)
        self.assertEqual(
            self.concrete_game.previous_player, self.concrete_game.player_1
        )
        self.assertEqual(self.concrete_game.current_player, self.concrete_game.player_2)

        # Player 2's Move (State Transition from Player 2 to 1)
        self.concrete_game.make_current_player_attack(0, 0)
        self.assertEqual(
            self.concrete_game.previous_player, self.concrete_game.player_2
        )
        self.assertEqual(self.concrete_game.current_player, self.concrete_game.player_1)

    def test_current_player_hits_target(self):
        """Test whether the current player successfully hits the target."""

        self.assertEqual(self.concrete_game.current_player, self.concrete_game.player_1)

        self.concrete_game.make_current_player_attack(0, 2)

        self.assertEqual(len(self.concrete_game.player_1.enemy_board.hit_cells), 1)

        player_1_hit_or_missed_board = (
            self.concrete_game.player_1.enemy_board.get_board_for_enemy()
        )
        self.assertEqual(player_1_hit_or_missed_board[0][2], "X")

    def test_current_player_missed_target(self):
        """Test whether the current player misses the target."""

        self.assertEqual(self.concrete_game.current_player, self.concrete_game.player_1)

        self.concrete_game.make_current_player_attack(0, 3)

        self.assertEqual(len(self.concrete_game.player_1.enemy_board.hit_cells), 0)

        player_1_hit_or_missed_board = (
            self.concrete_game.player_1.enemy_board.get_board_for_enemy()
        )
        self.assertEqual(player_1_hit_or_missed_board[0][3], "O")

    def test_current_player_wins_game(self):
        """Test whether the current player wins the game."""

        self.assertEqual(self.concrete_game.current_player, self.concrete_game.player_1)

        winner_or_none = self.concrete_game.get_winner()
        while winner_or_none is None:
            if self.concrete_game.current_player == self.concrete_game.player_1:
                try:
                    move = self.PLAYER_1_WINS_PLAYER_1_MOVES.pop(0)
                    self.concrete_game.make_current_player_attack(*move)
                except IndexError:
                    print("There are no more moves for Player 1.")

            elif self.concrete_game.current_player == self.concrete_game.player_2:
                try:
                    move = self.PLAYER_1_WINS_PLAYER_2_MOVES.pop(0)
                    self.concrete_game.make_current_player_attack(*move)
                except IndexError:
                    print("There are no more moves for Player 2.")

            winner_or_none = self.concrete_game.get_winner()

        self.assertIsInstance(winner_or_none, Player)
        self.assertEqual(winner_or_none, self.concrete_game.player_1)
        self.assertTrue(
            self.concrete_game.player_1.enemy_board.is_player_lost
        )  # Player 2 Lost
        self.assertFalse(
            self.concrete_game.player_2.enemy_board.is_player_lost
        )  # Player 1 Not Lost

    def test_current_player_loses_game(self):
        """Test whether the current player loses the game."""

        self.assertEqual(self.concrete_game.current_player, self.concrete_game.player_1)

        winner_or_none = self.concrete_game.get_winner()
        while winner_or_none is None:
            if self.concrete_game.current_player == self.concrete_game.player_1:
                try:
                    move = self.PLAYER_2_WINS_PLAYER_1_MOVES.pop(0)
                    self.concrete_game.make_current_player_attack(*move)
                except IndexError:
                    print("There are no more moves for Player 1.")

            elif self.concrete_game.current_player == self.concrete_game.player_2:
                try:
                    move = self.PLAYER_2_WINS_PLAYER_2_MOVES.pop(0)
                    self.concrete_game.make_current_player_attack(*move)
                except IndexError:
                    print("There are no more moves for Player 2.")

            winner_or_none = self.concrete_game.get_winner()

        self.assertIsInstance(winner_or_none, Player)
        self.assertEqual(winner_or_none, self.concrete_game.player_2)
        self.assertTrue(
            self.concrete_game.player_2.enemy_board.is_player_lost
        )  # Player 1 Lost
        self.assertFalse(
            self.concrete_game.player_1.enemy_board.is_player_lost
        )  # Player 2 Not Lost


if __name__ == "__main__":
    unittest.main()
