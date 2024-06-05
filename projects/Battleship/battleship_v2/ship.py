from typing import Set, Tuple, List
from exceptions import InvalidHitMoveException, InvalidShipCoordinateException


class Ship:
    def __init__(self, coordinates: List[Tuple[int, int]]):
        """
        Represents a ship on the game board.

        Attributes:
            coordinates (List[Tuple[int, int]]): The coordinates representing the position of the ship.
        """

        self.coordinates = coordinates
        self._check_ship_coordinates()

        self._un_hit_coordinates: Set[Tuple[int, int]] = {
            tup for tup in self.coordinates
        }

    @property
    def is_destroyed(self) -> bool:
        """
        Checks if the ship is destroyed.

        Returns:
            bool: True if the ship is destroyed, False otherwise.
        """
        return len(self._un_hit_coordinates) == 0

    @property
    def num_hits(self) -> int:
        """
        Returns the number of hits on the ship.

        Returns:
            int: Number of hits on the ship.
        """
        return len(self.hit_cells)

    @property
    def hit_cells(self) -> List[Tuple[int, int]]:
        """
        Returns the coordinates of the hit cells on the ship.

        Returns:
            List[Tuple[int, int]]: List of tuples representing the coordinates of the hit cells.
        """
        return list(set(self.coordinates) - self._un_hit_coordinates)

    @property
    def un_hit_cells(self) -> List[Tuple[int, int]]:
        """
        Returns the coordinates of the un-hit cells on the ship.

        Returns:
            List[Tuple[int, int]]: List of tuples representing the coordinates of the un-hit cells.
        """
        return list(self._un_hit_coordinates)

    def hit_ship(self, row, col) -> None:
        """
        Marks the specified cell on the ship as hit.

        Args:
            row (int): The row index of the cell to be hit.
            col (int): The column index of the cell to be hit.

        Raises:
            InvalidHitMoveException: If the specified cell is already hit or if the ship is already destroyed.
        """
        if self.is_destroyed:
            raise InvalidHitMoveException("The ship is already destroyed.")
        if (row, col) not in self._un_hit_coordinates:
            raise InvalidHitMoveException(
                f"{(row, col)} is an invalid hit move coordinate."
            )

        self._un_hit_coordinates.discard((row, col))

    def is_ship_overlap(self, other) -> bool:
        """
        Checks if the ship overlaps with another ship.

        Args:
            other (Ship): The other ship to check for overlap.

        Returns:
            bool: True if there is an overlap, False otherwise.

        Raises:
            ValueError: If the given ship is not of the same type as this ship.
        """
        if type(other) is not self.__class__:
            raise ValueError(
                f"The given ship is not of type `{self.__class__.__name__}`"
            )

        return any([tup in other.coordinates for tup in self.coordinates])

    def _check_ship_coordinates(self) -> None:
        """
        Checks if the ship's coordinates are valid.

        Raises:
            InvalidShipCoordinateException: If the ship's coordinates are invalid.
        """
        rows = sorted([tup[0] for tup in self.coordinates])
        columns = sorted([tup[1] for tup in self.coordinates])

        # Check if there are given coordinates for ship's position
        if len(self.coordinates) < 1:
            raise InvalidShipCoordinateException(
                "Cannot instantiate a ship without coordinates for it's position."
            )

        # Check if any of rows or columns are less than 0
        if any(row < 0 for row in rows):
            raise InvalidShipCoordinateException(
                "One of the ship's coordinates have negative row value."
            )
        if any(col < 0 for col in columns):
            raise InvalidShipCoordinateException(
                "One of the ship's coordinates have negative column value."
            )

        if len(self.coordinates) > 1:
            # Check if neither the rows nor columns have constant value
            is_row_constant = not any(
                [rows[j] != rows[j + 1] for j in range(len(rows) - 1)]
            )
            is_col_constant = not any(
                [columns[i] != columns[i + 1] for i in range(len(columns) - 1)]
            )

            if any([rows[j] != rows[j + 1] for j in range(len(rows) - 1)]) and any(
                [columns[i] != columns[i + 1] for i in range(len(columns) - 1)]
            ):
                raise InvalidShipCoordinateException(
                    "Neither the rows or columns have constant value."
                )

            # Check if there's a duplicate tuple in the coordinates
            if len(self.coordinates) != len(set(self.coordinates)):
                raise InvalidShipCoordinateException(
                    "There is a duplicate in one of the ship's coordinates."
                )

            # Check if the non-constant row/column is in consecutive order
            if is_row_constant:
                # The columns must be consecutive
                assert all(
                    [
                        columns[idx] + 1 == columns[idx + 1]
                        for idx in range(len(columns) - 1)
                    ]
                ), "The columns are not in consecutive order."
            if is_col_constant:
                # The rows must be consecutive
                assert all(
                    [rows[idx] + 1 == rows[idx + 1] for idx in range(len(rows) - 1)]
                ), "The rows are not in consecutive order."
