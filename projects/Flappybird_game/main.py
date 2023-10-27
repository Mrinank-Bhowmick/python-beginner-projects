import pygame, sys, random


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 512 - 75))
    screen.blit(floor_surface, (floor_x_pos + 200, 512 - 75))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos - 450))
    return bottom_pipe, top_pipe


def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 512:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 512 - 75:
        return False

    return True


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 5, 1)
    return new_bird


def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(50, bird_rect.centery))
    return new_bird, new_bird_rect


def score_display(game_state):
    if game_state == " main_game":
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288 / 2, 50))
        screen.blit(score_surface, score_rect)

    if game_state == "game_over":
        score_surface = game_font.render(f"Score:{int(score)}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288 / 2, 50))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(
            f" High Score:{int(high_score)}", True, (255, 255, 255)
        )
        high_score_rect = high_score_surface.get_rect(center=(288 / 2, 410))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


pygame.mixer.pre_init()
pygame.init()
screen = pygame.display.set_mode((288, 512))
Clock = pygame.time.Clock()
game_font = pygame.font.Font("assets/FlappyBirdy.ttf", 40)

# game var
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0

bg_surface = pygame.image.load("assets/background-night.png")


floor_surface = pygame.image.load("assets/base.png")
floor_x_pos = 0

bird_downflap = pygame.image.load("assets/bluebird.png").convert_alpha()
bird_midflap = pygame.image.load("assets/bluebird-midflap.png").convert_alpha()
bird_upflap = pygame.image.load("assets/bluebird-upflap.png").convert_alpha()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(50, 512 / 2))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

# bird_surface = pygame.image.load('bluebird-midflap.png').convert_alpha()
# bird_rect = bird_surface.get_rect(center = (50,512/2))

pipe_surface = pygame.image.load("assets/pipe-green.png")
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1000)
pipe_height = [200, 250, 300, 350, 400]

game_over_surface = pygame.image.load("assets/message.png")
game_over_rect = game_over_surface.get_rect(center=(288 / 2, 512 / 2))

flap_sound = pygame.mixer.Sound("assets/wing.ogg")
death_sound = pygame.mixer.Sound("assets/hit.ogg")
score_sound = pygame.mixer.Sound("assets/point.ogg")
score_sound_countdown = 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 5
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (50, 512 / 2)
                bird_movement = 0
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0

        bird_surface, bird_rect = bird_animation()

    screen.blit(bg_surface, (0, 0))

    if game_active:
        # bird
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # pipes
        pipe_list = move_pipe(pipe_list)
        draw_pipes(pipe_list)

        score += 0.01
        score_display("main_game")
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display("game_over")

    # floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -200:
        floor_x_pos = 0
    pygame.display.update()
    Clock.tick(60)
