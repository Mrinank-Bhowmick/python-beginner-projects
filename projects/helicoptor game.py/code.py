import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
HELICOPTER_WIDTH, HELICOPTER_HEIGHT = 50, 50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 200
HELICOPTER_SPEED = 5
OBSTACLE_SPEED = 5
WHITE = (255, 255, 255)
RED = (255, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Helicopter Racing Game")


helicopter_img = pygame.image.load("helicopter.png")
helicopter_img = pygame.transform.scale(helicopter_img, (HELICOPTER_WIDTH, HELICOPTER_HEIGHT))


helicopter_x = WIDTH // 4
helicopter_y = HEIGHT // 2 - HELICOPTER_HEIGHT // 2

obstacle_x = WIDTH
obstacle_y = 0

score = 0

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        helicopter_y -= HELICOPTER_SPEED
    if keys[pygame.K_DOWN]:
        helicopter_y += HELICOPTER_SPEED

    obstacle_x -= OBSTACLE_SPEED
    if obstacle_x + OBSTACLE_WIDTH < 0:
        obstacle_x = WIDTH
        obstacle_y = random.randint(0, HEIGHT - OBSTACLE_HEIGHT)
        score += 1

    window.fill(WHITE)
    pygame.draw.rect(window, RED, (obstacle_x, obstacle_y, OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
    window.blit(helicopter_img, (helicopter_x, helicopter_y))

    text = font.render(f"Score: {score}", True, RED)
    window.blit(text, (10, 10))

    if (helicopter_x + HELICOPTER_WIDTH > obstacle_x and helicopter_x < obstacle_x + OBSTACLE_WIDTH) and (helicopter_y < obstacle_y + OBSTACLE_HEIGHT and helicopter_y + HELICOPTER_HEIGHT > obstacle_y):
        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
