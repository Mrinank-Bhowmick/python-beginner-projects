import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Chrome Dinosaur Game")
icon = pygame.image.load("dino.png")
pygame.display.set_icon(icon)

dino = pygame.sprite.Sprite()
dino.image = pygame.image.load("dino.png")
dino.rect = dino.image.get_rect()
dino.rect.x = 100
dino.rect.y = 400
dino.vel_y = 0

cactus = pygame.sprite.Sprite()
cactus.image = pygame.image.load("cactus.png")
cactus.rect = cactus.image.get_rect()
cactus.rect.x = 800
cactus.rect.y = 400
cactus.vel_x = -5

sprites = pygame.sprite.Group()
sprites.add(dino)
sprites.add(cactus)

running = True

while running:
    screen.fill((255, 255, 255))

    sprites.draw(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if dino.rect.y == 400:
                    dino.vel_y = -15

    dino.rect.y += dino.vel_y
    dino.vel_y += 1

    if dino.rect.y > 400:
        dino.rect.y = 400
        dino.vel_y = 0

    cactus.rect.x += cactus.vel_x

    if cactus.rect.x < -100:
        cactus.rect.x = 800
        cactus.vel_x -= 1

    if pygame.sprite.collide_rect(dino, cactus):
        running = False
        print("Game Over")

pygame.quit()

