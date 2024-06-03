import unittest
from unittest.mock import patch, MagicMock
from game import Game
from constants import GameSettings, Point


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_init(self):
        self.assertIsNotNone(self.game.display)
        self.assertIsNotNone(self.game.snake)
        self.assertEqual(self.game.score, 0)
        self.assertIsNotNone(self.game.food)

    def test_is_collision(self):
        # Snake is out of bounds
        self.game.snake.head = Point(-1, -1)
        self.assertTrue(self.game.is_collision())
        # Snake collides with itself
        self.game.snake.head = self.game.snake.blocks[1]
        self.assertTrue(self.game.is_collision())

    @patch('pygame.event.get')
    @patch('pygame.draw.rect')
    @patch('pygame.display.flip')
    @patch('pygame.font.Font')
    def test_play_step(self, mock_event_get, mock_draw_rect, mock_display_flip, mock_font):
        mock_event_get.return_value = []
        mock_font_instance = MagicMock()
        mock_font_instance.render.return_value = MagicMock()
        mock_font.return_value = mock_font_instance

        init_snake_length = len(self.game.snake.blocks)
        init_score = self.game.score
        init_head_position = self.game.snake.head
        # Place food in front of snake
        self.game.food = Point(init_head_position.x + GameSettings.BLOCK_SIZE, init_head_position.y)
        self.game.play_step()

        self.assertEqual(len(self.game.snake.blocks), init_snake_length + 1)
        self.assertEqual(self.game.score, init_score + 1)
        new_head_position = Point(init_head_position.x + GameSettings.BLOCK_SIZE, init_head_position.y)
        self.assertEqual(self.game.snake.head, new_head_position)

    def test_place_food(self):
        self.game.place_food()
        self.assertNotIn(self.game.food, self.game.snake.blocks)


if __name__ == '__main__':
    unittest.main()
