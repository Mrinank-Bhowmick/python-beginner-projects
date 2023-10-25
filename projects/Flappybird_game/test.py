import unittest
import pygame

class TestGameFont(unittest.TestCase):
    def test_font_creation(self):
        pygame.init()

        #Create a font object using the 'pygame.font.Font' function
        game_font = pygame.font.Font("flappy-bird.ttf", 40)

        #To varify whether a game_font object is an instance of pygame.font.Font
        self.assertIsInstance(game_font, pygame.font.Font)

if __name__ == '__main__':
    unittest.main()
