import pygame
import sys
import random


class Block(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))


class Player(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed
        self.movement = 0
        self.x = x_pos

    def screen_constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def update(self, bll_group):
        self.rect.y += self.movement
        self.screen_constrain()


class Opponent(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed
        self.x = x_pos

    def update(self, ball_group):
        if game_state.state == "hard_game" or game_state.state == "med_game":
            if self.rect.center[1] < ball_group.sprite.rect.y:
                self.rect.y += self.speed
            if self.rect.center[1] > ball_group.sprite.rect.y:
                self.rect.y -= self.speed
            self.constrain()
        else:
            if self.rect.top < ball_group.sprite.rect.y:
                self.rect.y += self.speed
            if self.rect.bottom > ball_group.sprite.rect.y:
                self.rect.y -= self.speed
            self.constrain()

    def constrain(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Ball(Block):
    def __init__(self, path, x_pos, y_pos, speed_x, speed_y, paddles):
        super().__init__(path, x_pos, y_pos)
        self.speed_x = speed_x * random.choice((-1, 1))
        self.speed_y = speed_y * random.choice((-1, 1))
        self.paddles = paddles
        self.active = False
        self.score_time = 0

    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()
        else:
            self.restart_counter()

    def collisions(self):
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            pygame.mixer.Sound.play(hit_sound)
            self.speed_y *= -1

        if pygame.sprite.spritecollide(self, self.paddles, False):
            pygame.mixer.Sound.play(hit_sound)
            collision_paddle = pygame.sprite.spritecollide(self, self.paddles, False)[
                0
            ].rect
            if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1
            if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_paddle.bottom
                self.speed_y *= -1
            if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_x > 0:
                self.rect.bottom = collision_paddle.top
                self.speed_y *= -1

    def reset_ball(self):
        for paddle in self.paddles:
            if paddle.x == 20:
                paddle.rect.center = (20, HEIGHT / 2)
            else:
                paddle.rect.center = (WIDTH - 20, HEIGHT / 2)
        self.active = False
        self.speed_x *= random.choice((-1, 1))
        self.speed_y *= random.choice((-1, 1))
        self.score_time = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        if started > 1:
            pygame.mixer.Sound.play(score_sound)

    def restart_counter(self):
        current_time = pygame.time.get_ticks()
        countdown_number = 3

        if current_time - self.score_time <= 700:
            countdown_number = 3
        if 700 < current_time - self.score_time <= 1400:
            countdown_number = 2
        if 1400 < current_time - self.score_time <= 2100:
            countdown_number = 1
        if current_time - self.score_time >= 2100:
            self.active = True

        time_counter = game_font.render(str(countdown_number), True, accent_color)
        time_counter_rect = time_counter.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 50))
        pygame.draw.rect(WIN, bg_color, time_counter_rect)
        WIN.blit(time_counter, time_counter_rect)


class Game_Manager:
    def __init__(self, ball_group, paddle_group) -> None:
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.paddle_group = paddle_group

    def run_game(self):
        # Drawing Game Objects
        self.paddle_group.draw(WIN)
        self.ball_group.draw(WIN)

        # Updating the game objects
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()

    def reset_ball(self):
        if self.ball_group.sprite.rect.left >= WIDTH:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.right <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()

    def draw_score(self):
        player_score = game_font.render(str(self.player_score), True, accent_color)
        opponent_score = game_font.render(str(self.opponent_score), True, accent_color)

        player_score_rect = player_score.get_rect(midleft=(WIDTH / 2 + 40, HEIGHT / 2))
        opponent_score_rect = opponent_score.get_rect(
            midright=(WIDTH / 2 - 40, HEIGHT / 2)
        )

        WIN.blit(player_score, player_score_rect)
        WIN.blit(opponent_score, opponent_score_rect)


class Cursor(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.cursor_image = pygame.image.load("assets/cursor.png")
        self.cursor = pygame.transform.scale(self.cursor_image, (27, 27))
        self.cursor_rect = self.cursor.get_rect()

    def update(self):
        self.cursor_rect.topleft = pygame.mouse.get_pos()
        WIN.blit(self.cursor, self.cursor_rect)


class Options:
    def __init__(self, text, x, y) -> None:
        self.text = menu_font.render(text, True, (255, 255, 255))
        self.val = text
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 224, 74)
        self.text_rect = self.text.get_rect(center=(self.x + 112, self.y + 37))

    def draw(self):
        global opponent_speed, ball_speed, start_game
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.val == "EASY":
                    game_state.state = "easy_game"
                elif self.val == "MEDIUM":
                    game_state.state = "med_game"
                elif self.val == "HARD":
                    game_state.state = "hard_game"

        pygame.draw.rect(WIN, (59, 59, 209), self.rect)
        WIN.blit(self.text, self.text_rect)


class GameState:
    def __init__(self) -> None:
        self.state = "menu"

    def start_game(self):
        if self.state == "menu":
            self.menu()
        elif self.state == "easy_game":
            self.easy_game()
        elif self.state == "med_game":
            self.med_game()
        elif self.state == "hard_game":
            self.hard_game()

    def menu(self):
        WIN.fill(bg_color)
        WIN.blit(menu_head, menu_head_rect)
        easy.draw()
        medium.draw()
        hard.draw()
        cursor.update()
        pygame.display.flip()

    def easy_game(self):
        global created, FPS, started
        if created:
            create_ball()
            ball.reset_ball()
            started = 2
            created = False
        FPS = 110
        pygame.draw.rect(WIN, accent_color, middle_strip)
        cursor.update()
        game_manager.run_game()

    def med_game(self):
        global FPS, ball_speed, created, started
        opponent.speed = 8
        if created:
            create_ball()
            ball.reset_ball()
            started = 2
            created = False
        FPS = 140
        pygame.draw.rect(WIN, accent_color, middle_strip)
        cursor.update()
        game_manager.run_game()

    def hard_game(self):
        global FPS, ball_speed, created, started
        opponent.speed = 10
        if created:
            create_ball()
            ball.reset_ball()
            started = 2
            created = False
        ball_speed = 20
        FPS = 170
        pygame.draw.rect(WIN, accent_color, middle_strip)
        cursor.update()
        game_manager.run_game()


def create_ball():
    global ball, ball_sprite, game_manager
    ball = Ball(
        "assets/ball.png",
        WIDTH / 2,
        HEIGHT / 2,
        4,
        4,
        paddle_group,
    )
    ball_sprite = pygame.sprite.GroupSingle()
    ball_sprite.add(ball)

    game_manager = Game_Manager(ball_sprite, paddle_group)


# General Setup
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# Main Window
WIDTH = 1000
HEIGHT = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

created = True
started = 1

# Global Variables
bg_color = pygame.Color("#2f373f")
accent_color = (27, 35, 43)
game_font = pygame.font.Font("freesansbold.ttf", 32)
menu_font = pygame.font.Font("assets/Arcade_N.ttf", 32)
hit_sound = pygame.mixer.Sound("assets/hit.wav")
score_sound = pygame.mixer.Sound("assets/score.wav")
middle_strip = pygame.Rect(WIDTH / 2 - 2, 0, 4, HEIGHT)
start_game = False
pygame.mouse.set_visible(False)


# level Dependent Variables

opponent_speed = 5
FPS = 110

# Game Objects
player = Player(
    "assets/paddle.png",
    WIDTH - 20,
    HEIGHT / 2,
    5,
)
opponent = Opponent(
    "assets/paddle.png",
    20,
    HEIGHT / 2,
    opponent_speed,
)
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)


game_cursor = Cursor()
cursor = pygame.sprite.GroupSingle()
cursor.add(game_cursor)


menu_head = menu_font.render("Difficulty", True, (68, 152, 252))
menu_head_rect = menu_head.get_rect(center=(WIDTH / 2, 150))

# # Options
easy = Options("EASY", WIDTH / 2 - 112, 241)
medium = Options("MEDIUM", WIDTH / 2 - 112, 365)
hard = Options("HARD", WIDTH / 2 - 112, 489)

game_state = GameState()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.movement -= player.speed
            if event.key == pygame.K_DOWN:
                player.movement += player.speed
            if event.key == pygame.K_ESCAPE:
                game_state.state = "menu"
                created = True
                started = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.movement += player.speed
            if event.key == pygame.K_DOWN:
                player.movement -= player.speed

    # Background Stuff
    WIN.fill(bg_color)

    game_state.start_game()

    # Rendering
    pygame.display.flip()
    clock.tick(FPS)
