import unittest
import pygame

class TestGameFont(unittest.TestCase):
    def test_font_creation(self):
        pygame.init()
        game_font = pygame.font.Font("flappy-bird.ttf", 40)
        self.assertIsInstance(game_font, pygame.font.Font)
        # You can add more specific assertions if needed

if __name__ == '__main__':
    unittest.main()
