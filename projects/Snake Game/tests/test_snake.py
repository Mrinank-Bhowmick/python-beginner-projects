import unittest
from snake import Snake, Point, Direction
from constants import GameSettings


class TestSnake(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()

    def test_init(self):
        self.assertEqual(
            self.snake.head, Point(GameSettings.WIDTH / 2, GameSettings.HEIGHT / 2)
        )
        self.assertEqual(self.snake.block_size, GameSettings.BLOCK_SIZE)
        self.assertEqual(len(self.snake.blocks), 3)
        self.assertEqual(self.snake.direction, Direction.RIGHT)

    def test_move(self):
        init_head = self.snake.head
        self.snake.move(Direction.RIGHT)
        new_head_position = Point(init_head.x + GameSettings.BLOCK_SIZE, init_head.y)
        self.assertEqual(self.snake.head, new_head_position)
        self.assertEqual(self.snake.blocks[0], new_head_position)

    def test_self_collision(self):
        self.snake.head = Point(100, 100)
        self.snake.blocks = [
            self.snake.head,
            Point(80, 100),
            Point(60, 100),
            Point(100, 100),
        ]
        self.assertTrue(self.snake.self_collision())


if __name__ == "__main__":
    unittest.main()
