import pygame
from constants import RgbColors, GameSettings


class Display:
    """Manages the display of the game."""

    def __init__(self):
        pygame.init()
        self.width = GameSettings.WIDTH
        self.height = GameSettings.HEIGHT
        self.font = pygame.font.Font(None, 25)
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()

    def update_ui(self, snake, food, score, high_score):
        """Updates the UI with the current game state.

        Args:
            snake (Snake): The snake object that contains the snake body (Snake.blocks).
            food (Point): The food object to be displayed.
            score (int): The current game score.
            high_score: The highest score achieved so far.
        """
        self.window.fill(RgbColors.BLACK)
        self.draw_snake(snake)
        self.draw_food(food)
        self.draw_score(score)
        self.render_high_score(high_score)
        pygame.display.flip()

    def draw_snake(self, snake):
        for block in snake.blocks:
            pygame.draw.rect(
                self.window,
                RgbColors.BLUE1,
                pygame.Rect(
                    block.x, block.y, GameSettings.BLOCK_SIZE, GameSettings.BLOCK_SIZE
                ),
            )
            pygame.draw.rect(
                self.window,
                RgbColors.BLUE2,
                pygame.Rect(block.x + 4, block.y + 4, 12, 12),
            )

    def draw_food(self, food):
        pygame.draw.rect(
            self.window,
            RgbColors.RED,
            pygame.Rect(
                food.x, food.y, GameSettings.BLOCK_SIZE, GameSettings.BLOCK_SIZE
            ),
        )

    def draw_score(self, score):
        self.font = pygame.font.Font(None, 25)
        score_display = self.font.render(f"Score: {score}", True, RgbColors.WHITE)
        self.window.blit(score_display, [0, 0])

    def render_game_over(self):
        self.font = pygame.font.Font(None, 48)
        game_over_display = self.font.render("GAME OVER", True, RgbColors.WHITE)
        text_width = game_over_display.get_width()
        text_height = game_over_display.get_height()
        text_x = (self.width - text_width) // 2
        text_y = (self.height // 4) - (text_height // 2)
        self.window.blit(game_over_display, [text_x, text_y])
        pygame.display.flip()

    def render_play_again(self):
        self.font = pygame.font.Font(None, 32)
        play_again_display = self.font.render(
            "Play again? (Y/N)", True, RgbColors.WHITE
        )
        display_box = play_again_display.get_rect(
            center=(self.width // 2, self.height // 2)
        )
        self.window.blit(play_again_display, display_box)
        pygame.display.flip()

    def render_high_score(self, high_score):
        high_score_display = self.font.render(
            f"High Score: {high_score}", True, RgbColors.WHITE
        )
        self.window.blit(
            high_score_display, [self.width - high_score_display.get_width(), 0]
        )

    def render_new_high_score(self, new_high_score):
        new_high_score_display = self.font.render(
            f"New High Score: {new_high_score}", True, RgbColors.WHITE
        )
        text_width = new_high_score_display.get_width()
        text_height = new_high_score_display.get_height()
        text_x = (self.width - text_width) // 2
        text_y = (self.height // 3) - (text_height // 2)
        self.window.blit(new_high_score_display, [text_x, text_y])
        pygame.display.flip()
