class BattleshipException(Exception):
    """Base Class for Battleship Exceptions"""


class InvalidShipCoordinateException(BattleshipException):
    """Raises error when a ship's coordinates are invalid."""


class InvalidHitMoveException(BattleshipException):
    """Raises error when a player tries to give an invalid hit move coordinate."""


class BoardException(BattleshipException):
    """Base class for exceptions related to the game board."""


class GameException(BattleshipException):
    """Base class for general exceptions related to the Battleship game."""
