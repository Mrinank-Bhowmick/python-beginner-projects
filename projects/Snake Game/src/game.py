import pygame
import random
import json
from snake import Snake, Direction, Point
from display import Display
from constants import GameSettings


class Game:
    """Manages the gameplay logic and its user interactions."""

    def __init__(self):
        self.display = Display()
        self.snake = Snake()
        self.score = 0
        self.food = None
        self.place_food()
        self.high_score = self.load_high_score()

    def game_loop(self):
        while True:
            self.play_step()
            game_over, score = self.play_step()
            self.update_high_score(self.high_score)
            if game_over:
                self.display.render_game_over()
                if score > self.high_score:
                    self.display.render_new_high_score(score)
                    self.update_high_score(score)
                    self.high_score = self.load_high_score()
                self.display.render_play_again()
                if not self.play_again():
                    break
                self.restart_game()
        pygame.quit()

    def is_collision(self):
        """Checks if the snake has collided with the boundary or with itself.

        Returns:
            bool: True if a collision is detected, False otherwise.
        """
        # Snake hits boundary
        if (
            self.snake.head.x > self.display.width - self.snake.block_size
            or self.snake.head.x < 0
            or self.snake.head.y > self.display.height - self.snake.block_size
            or self.snake.head.y < 0
        ):
            return True
        # Snake hits itself
        if self.snake.self_collision():
            return True
        return False

    def game_over(self):
        return self.is_collision()

    def get_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snake.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.snake.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.snake.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.snake.direction = Direction.DOWN

    def play_step(self):
        """Executes one step through the game."""
        self.get_user_input()
        self.snake.move(self.snake.direction)
        if self.snake.head == self.food:
            self.score += 1
            self.place_food()
        else:
            self.snake.blocks.pop()
        # Update UI and Clock
        self.display.update_ui(self.snake, self.food, self.score, self.high_score)
        self.display.clock.tick(GameSettings.SPEED)
        game_over = self.is_collision()
        return game_over, self.score

    def place_food(self):
        """Randomly places the food on the screen."""
        x = (
            random.randint(
                0,
                (self.display.width - GameSettings.BLOCK_SIZE)
                // GameSettings.BLOCK_SIZE,
            )
            * GameSettings.BLOCK_SIZE
        )
        y = (
            random.randint(
                0,
                (self.display.height - GameSettings.BLOCK_SIZE)
                // GameSettings.BLOCK_SIZE,
            )
            * GameSettings.BLOCK_SIZE
        )
        self.food = Point(x, y)
        if self.food in self.snake.blocks:
            self.place_food()

    def play_again(self):
        """Asks the user to play again or quit the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_n, pygame.K_ESCAPE]:
                        return False
                    if event.key in [pygame.K_y, pygame.K_RETURN]:
                        return True

    def restart_game(self):
        """Resets the state of the game."""
        self.snake = Snake()
        self.score = 0
        self.place_food()
        self.high_score = self.load_high_score()

    def load_high_score(self):
        """Loads the high score from a JSON file."""
        try:
            with open("high_score.json", "r") as file:
                data = json.load(file)
                return data.get("high_score")
        except FileNotFoundError:
            return 0

    def update_high_score(self, new_score):
        """Updates the high score in the JSON file if the new score is greater than the current high score."""
        high_score = self.load_high_score()
        if new_score > high_score:
            data = {"high_score": new_score}
            with open("high_score.json", "w") as file:
                json.dump(data, file)
