import pygame
from constants import RgbColors, GameSettings


class Display:
    def __init__(self):
        pygame.init()
        self.width = GameSettings.WIDTH
        self.height = GameSettings.HEIGHT
        self.font = pygame.font.Font(None, 25)
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

    def update_ui(self, snake, food, score):
        self.window.fill(RgbColors.BLACK)
        # Draw snake
        for block in snake.blocks:
            pygame.draw.rect(
                self.window, RgbColors.BLUE1,
                pygame.Rect(block.x, block.y, GameSettings.BLOCK_SIZE, GameSettings.BLOCK_SIZE)
            )
            pygame.draw.rect(
                self.window, RgbColors.BLUE2, pygame.Rect(block.x + 4, block.y + 4, 12, 12)
            )
        # Draw food
        pygame.draw.rect(
            self.window,
            RgbColors.RED,
            pygame.Rect(food.x, food.y, GameSettings.BLOCK_SIZE, GameSettings.BLOCK_SIZE),
        )
        # Draw score
        score_display = self.font.render(f"Score: {score}", True, RgbColors.WHITE)
        self.window.blit(score_display, [0, 0])  # score in top left corner of window
        pygame.display.flip()
