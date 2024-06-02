from constants import GameSettings, Direction, Point


class Snake:
    def __init__(self, init_length=3):
        self.head = Point(GameSettings.WIDTH / 2, GameSettings.HEIGHT / 2)
        self.block_size = GameSettings.BLOCK_SIZE
        self.blocks = ([self.head] +
                       [Point(self.head.x - (i * self.block_size), self.head.y) for i in range(1, init_length)])
        self.direction = Direction.RIGHT

    def move(self, direction):
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
        if self.head in self.blocks[1:]:
            return True
        return False
