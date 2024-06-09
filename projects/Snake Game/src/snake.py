from constants import GameSettings, Direction, Point


class Snake:
    """Represents the snake in the game."""

    def __init__(self, init_length=3):
        """Initializes the snake.

        Args:
            init_length (int): Length of the snake on initialization.
        """
        self.head = Point(GameSettings.WIDTH / 2, GameSettings.HEIGHT / 2)
        self.block_size = GameSettings.BLOCK_SIZE
        self.blocks = [self.head] + [
            Point(self.head.x - (i * self.block_size), self.head.y)
            for i in range(1, init_length)
        ]
        self.direction = Direction.RIGHT

    def move(self, direction):
        """Moves the snake in the given direction.

        Args:
            direction (Direction): The direction to move the snake.

        Returns:
            Point: The new snake head position.
        """
        x, y = self.head
        if direction == Direction.RIGHT:
            x += self.block_size
        elif direction == Direction.LEFT:
            x -= self.block_size
        elif direction == Direction.DOWN:
            y += self.block_size
        elif direction == Direction.UP:
            y -= self.block_size
        self.head = Point(x, y)
        self.blocks.insert(0, self.head)
        return self.head

    def self_collision(self):
        """Checks if the snake collides with itself.

        Returns:
            bool: True if the snake collides with its body, False otherwise.
        """
        if self.head in self.blocks[1:]:
            return True
        return False
