import pygame
import random

# setup
pygame.init()
pygame.mixer.pre_init(44100,-16,2,512)
clock = pygame.time.Clock()

# Main Screen
WIDTH, HEIGHT = 1000, 680
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG GAME")

#Sounds
pong_sound=pygame.mixer.Sound("pong.ogg")
score_sound= pygame.mixer.Sound("score.ogg")
# colors
RED = (255, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
Navy = (0, 0, 128)
LIGHT_GREY = (200, 200, 200)

# Game Rectangles
ball_width, ball_height = 30, 30
ball = pygame.Rect(int(WIDTH / 2 - ball_width / 2), int(HEIGHT / 2 - ball_height / 2), ball_width,
                   ball_height)  # (Left,Top, Width ,Height)

player_widht, player_height = 10, 140
player = pygame.Rect(int(WIDTH - player_widht * 2), int(HEIGHT / 2 - player_height / 2), player_widht, player_height)

opponent_widht, opponent_height = 10, 140
opponent = pygame.Rect(10, int(HEIGHT / 2 - 70), opponent_widht, opponent_height)

# Background features
BACKGROUND_COLOR = pygame.Color('grey12')

# Movements
ball_speed_X = 7 * random.choice((1, -1))
ball_speed_Y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 30)  # Font name, font size

# Time Variables
score_time = True


def ball_restart():
    global ball_speed_X, ball_speed_Y, score_time

    current_time = pygame.time.get_ticks()
    time = current_time - score_time
    ball.center = (int(WIDTH / 2), int(HEIGHT / 2))

    if time < 700:
        number_three = game_font.render("3", 0, BLUE)
        SCREEN.blit(number_three, (int(WIDTH / 2 - 10), int(HEIGHT / 2 + 20)))
    if 700 < time < 1400:
        number_two = game_font.render("2", 0, RED)
        SCREEN.blit(number_two, (int(WIDTH / 2 - 10), int(HEIGHT / 2 + 20)))
    if 1400 < time < 2100:
        number_one = game_font.render("1", 0, GREEN)
        SCREEN.blit(number_one, (int(WIDTH / 2 - 10), int(HEIGHT / 2 + 20)))

    if time < 2100:
        ball_speed_X, ball_speed_Y = 0, 0
    else:
        ball_speed_X = 7 * random.choice((1, -1))
        ball_speed_Y = 7 * random.choice((1, -1))
        score_time = None

    ball_speed_Y *= random.choice((1, -1))
    ball_speed_X *= random.choice((1, -1))


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT


def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT


def ball_animation():
    global ball_speed_X, ball_speed_Y, opponent_score, player_score, score_time
    ball.x += ball_speed_X
    ball.y += ball_speed_Y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_Y *= -1

    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

        # Opponent Score
    if ball.right >= WIDTH:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_X > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_X *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_Y > 0:
            ball_speed_Y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_Y < 0:
            ball_speed_Y *= -1

    if ball.colliderect(opponent) and ball_speed_X < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_X *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_Y > 0:
            ball_speed_Y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_Y < 0:
            ball_speed_Y *= -1


# Game LOOP
running = True
while running:
    clock.tick(60)
    # Handling the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

    # Visuals
    SCREEN.fill(BACKGROUND_COLOR)
    pygame.draw.rect(SCREEN, LIGHT_GREY, player)
    pygame.draw.rect(SCREEN, LIGHT_GREY, opponent)
    pygame.draw.ellipse(SCREEN, LIGHT_GREY, ball)
    pygame.draw.aaline(SCREEN, LIGHT_GREY, (WIDTH / 2, 0), (
        WIDTH / 2, HEIGHT))  # IN First tuple (width/2) means at middle and 0 means starting height(from top)
    # Second tuple means where to end the line so width/2,height will be straight with first tuple.

    if score_time:
        ball_restart()

    player_text = game_font.render(f'{player_score}', False, LIGHT_GREY)
    SCREEN.blit(player_text, (520, 320))

    opponent_text = game_font.render(f'{opponent_score}', False, LIGHT_GREY)
    SCREEN.blit(opponent_text, (465, 320))

    # Updating the Screen
    pygame.display.flip()

pygame.quit()
