import unittest
from unittest.mock import patch, MagicMock
import pygame
import pygame.time
from display import Display
from constants import RgbColors, GameSettings, Point
from snake import Snake


class TestDisplay(unittest.TestCase):

    def setUp(self):
        self.display = Display()
        self.snake = Snake()

    @patch('pygame.init')
    @patch('pygame.font.Font')
    @patch('pygame.display.set_mode')
    @patch('pygame.display.set_caption')
    @patch('pygame.time.Clock')
    def test_init(self, mock_init, mock_font, mock_set_mode, mock_set_caption, mock_clock):
        mock_init.return_value = True
        mock_font_instance = MagicMock()
        mock_font.return_value = mock_font_instance
        mock_window = MagicMock()
        mock_set_mode.return_value = mock_window
        mock_clock_instance = MagicMock()
        mock_clock.return_value = mock_clock_instance

        mock_set_mode.assert_called_with((GameSettings.WIDTH, GameSettings.HEIGHT))
        mock_set_caption.assert_called_with("Snake")
        mock_clock.assert_called()

        self.assertEqual(self.display.width, GameSettings.WIDTH)
        self.assertEqual(self.display.height, GameSettings.HEIGHT)
        self.assertIsInstance(self.display.font, pygame.font.Font)
        self.assertIsInstance(self.display.window, MagicMock)
        self.assertIsInstance(self.display.clock, MagicMock)

    @patch('pygame.init')
    @patch('pygame.display.set_mode')
    @patch('pygame.display.set_caption')
    @patch('pygame.font.Font')
    @patch('pygame.time.Clock')
    def test_init(self, mock_clock, mock_font, mock_set_caption, mock_set_mode, mock_init):
        display = Display()
        mock_init.assert_called_once()
        mock_font.assert_called_once()
        mock_set_caption.assert_called_with("Snake")
        mock_set_mode.assert_called_with((GameSettings.WIDTH, GameSettings.HEIGHT))
        mock_clock.assert_called_once()

        self.assertIsInstance(display.font, MagicMock)
        self.assertIsInstance(display.window, MagicMock)
        self.assertIsInstance(display.clock, MagicMock)

    @patch('pygame.draw.rect')
    @patch('pygame.font.Font')
    @patch('pygame.display.flip')
    @patch('pygame.display.set_mode')
    def test_update_ui(self, mock_set_mode, mock_display_flip, mock_font, mock_draw_rect):
        mock_window = mock_set_mode.return_value
        mock_font_instance = mock_font.return_value
        mock_font_instance.render = MagicMock()

        self.food = Point(100, 100)
        self.score = 10
        self.display.window = mock_window
        self.display.font = mock_font_instance
        self.display.update_ui(self.snake, self.food, self.score)

        mock_draw_rect.assert_called()
        mock_font_instance.render.assert_called()
        mock_display_flip.assert_called()


if __name__ == '__main__':
    unittest.main()
