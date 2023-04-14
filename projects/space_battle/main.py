import pygame
import random
import math
from pygame import mixer
from pygame import mixer_music

# initialise the game
pygame.init()
# create a screen
p = True


def play():
    screen = pygame.display.set_mode((800, 600))
    running = True
    pygame.display.set_caption("Space invaders")
    icon = pygame.image.load("ufo.png")
    pygame.display.set_icon(icon)
    player_image = pygame.image.load("resize-16681994301185496102ufo1.png")
    playerX = 200
    playerY = 400
    player_change = 0
    player_changeY = 0
    enemy_img = pygame.image.load("icons8-ufo-64.png")
    enemyN = 10
    img_list = []
    enemyX = []
    enemyY = []
    touch8 = []
    temp = []
    d = []
    d2 = []
    bullet = pygame.image.load("yellow_ball.png")
    bg = pygame.image.load("2352.jpg")
    Release = False
    bulletX = playerX + 8
    count = 0

    font = pygame.font.Font("freesansbold.ttf", 32)
    textX = 10
    textY = 10
    xchange = 0.3
    ychange = 25

    def bg_image(bg):
        screen.blit(bg, (0, 0))

    for t in range(enemyN):
        img_list.append(enemy_img)
        enemyX.append(random.randint(0, 700))
        enemyY.append(random.randint(0, 150))
        touch8.append(True)
        temp.append(True)
        d.append(100)
        d2.append(100)
    impact = False

    def show_score(x, y):
        count1 = font.render(("score:" + str(count)), True, (220, 34, 120))
        screen.blit(count1, (x, y))

    def game_over(x, y):
        over = font.render(
            "Game-Over\nYour Final Score is:" + str(count), True, (240, 140, 220)
        )
        screen.blit(over, (x, y))

    m1 = mixer.Sound("space-120280.mp3")

    m1.play(-1)

    def enemy(x, y, img_list):
        for t in range(enemyN):
            screen.blit(img_list[t], (enemyX[t], enemyY[t]))

    def bulletP(x, y):
        screen.blit(bullet, (x, y))

    def player(x, y):
        screen.blit(player_image, (x, y))

    def restart(x, y):
        res = font.render("TO play Again Press 1", True, (240, 140, 220))
        screen.blit(res, (x, y))

    bulletY = playerY - 30

    while running:
        screen.fill((10, 6, 150))
        bg_image(bg)
        move = False
        if count > 5:
            xchange = 0.4
            ychange = 45
        if count > 10:
            xchange = 0.6
            ychange = 55

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                p = False
            if event.type == pygame.KEYDOWN:
                move = True
                if event.key == pygame.K_LEFT:
                    player_change = -0.2
                if event.key == pygame.K_RIGHT:
                    player_change = 0.2
                if event.key == pygame.K_UP:
                    player_changeY = -0.2
                if event.key == pygame.K_DOWN:
                    player_changeY = 0.2
                if event.key == pygame.K_SPACE:
                    Release = True
                if event.key == pygame.K_1:
                    for l in range(enemyN):
                        enemyY[l] = random.randint(0, 150)
                        count = 0
                    playerY = 400
                    playerX = 200

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                    player_change = 0
                if event.key == pygame.K_UP or pygame.K_DOWN:
                    player_changeY = 0

        for i in range(enemyN):
            d2[i] = math.sqrt((enemyX[i] - playerX) ** 2 + (enemyY[i] - playerY) ** 2)

            if touch8[i] and i < enemyN / 2:
                enemyX[i] += xchange
            if touch8[i] == False and i < enemyN / 2:
                enemyX[i] -= xchange
            if temp[i] and i >= enemyN / 2:
                enemyX[i] -= xchange
            if temp[i] == False and i >= enemyN / 2:
                enemyX[i] += xchange
            if enemyX[i] > 750:
                touch8[i] = False
                temp[i] = True
                enemyY[i] += ychange
            if enemyX[i] < 20:
                touch8[i] = True
                temp[i] = False
                enemyY[i] += ychange

            if enemyY[i] > 480:
                for j in range(enemyN):
                    enemyY[j] = 2000
                game_over(100, 100)
                restart(80, 200)
                break

            d[i] = math.sqrt((enemyX[i] - bulletX) ** 2 + (enemyY[i] - bulletY) ** 2)

            if d[i] < 20:
                enemyX[i] = random.randint(0, 700)
                enemyY[i] = random.randint(0, 150)
                impact = True
                count = count + 1
                Release = False
                m2 = mixer.music.load("shotgun-firing-4-6746.mp3")
                mixer.music.play()

            else:
                impact = False
            if d2[i] < 60:
                for j in range(enemyN):
                    enemyY[j] = 2000
                game_over(100, 100)
                restart(50, 200)

        playerX += player_change
        if playerX > 750 or playerX < 0:
            player_change = 0
        playerY += player_changeY
        if playerY > 550 or playerY < 0:
            player_changeY = 0
        if bulletY < 0:
            bulletY = playerY - 30
            bulletX = playerX + 8
            Release = False
        if Release:
            bulletY -= 0.8
        else:
            bulletY = playerY - 30
            bulletX = playerX + 8

        player(playerX, playerY)
        bulletP(bulletX, bulletY)

        enemy(enemyX, enemyY, img_list)
        show_score(textX, textY)

        pygame.display.update()


if p:
    play()
