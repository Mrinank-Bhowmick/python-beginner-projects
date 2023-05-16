# Car Game by Pratyusha Chaturvedi
# Note: Pls download the images to run the game

import pygame, sys  # pip install pygame

pygame.init()  # initializes the Pygame
from pygame.locals import *  # import all modules from Pygame
import random
import math
import time

screen = pygame.display.set_mode((798, 600))

# initializing pygame mixer
pygame.mixer.init()

# changing title of the game window
pygame.display.set_caption("Furious Wheels")

# changing the logo
logo = pygame.image.load("logo.png")
pygame.display.set_icon(logo)


############ MAKING INTRO SCREEEN ###########
IntroFont = pygame.font.Font("freesansbold.ttf", 38)


def introImg(x, y):
    intro = pygame.image.load("intro.png")

    screen.blit(intro, (x, y))


def instructionIMG(x, y):
    instruct = pygame.image.load("instruction.png")
    run = True
    while run:
        screen.blit(instruct, (x, y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def aboutIMG(x, y):
    aboutimg = pygame.image.load("About.png")
    run = True
    while run:
        screen.blit(aboutimg, (x, y))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def play(x, y):
    playtext = IntroFont.render("PLAY", True, (255, 0, 0))
    screen.blit(playtext, (x, y))


def ABOUT(x, y):
    aboutText = IntroFont.render("ABOUT", True, (255, 0, 0))
    screen.blit(aboutText, (x, y))


def Instruction(x, y):
    instructionText = IntroFont.render("INSTRUCTION", True, (255, 0, 0))
    screen.blit(instructionText, (x, y))


def introscreen():
    run = True
    pygame.mixer.music.load("startingMusic.mp3")
    pygame.mixer.music.play()
    while run:
        screen.fill((0, 0, 0))
        introImg(0, 0)
        play(100, 450)
        Instruction(280, 450)
        ABOUT(615, 450)

        ####### getting coordinates of mouse cursor #######
        x, y = pygame.mouse.get_pos()

        ###### storing rectangle coordinates (x, y, length, height) by making variables
        button1 = pygame.Rect(60, 440, 175, 50)
        button2 = pygame.Rect(265, 440, 300, 50)
        button3 = pygame.Rect(600, 440, 165, 50)

        ##### Drawing rectangles with stored coorditates of rectangles.######
        ###### pygame.draw.rect takes these arguments (surface, color, coordinates, border) #####
        pygame.draw.rect(screen, (255, 255, 255), button1, 6)
        pygame.draw.rect(screen, (255, 255, 255), button2, 6)
        pygame.draw.rect(screen, (255, 255, 255), button3, 6)

        #### if our cursor is on button1 which is PLAY button
        if button1.collidepoint(x, y):
            ### changing from inactive to active by changing the color from white to red
            pygame.draw.rect(screen, (155, 0, 0), button1, 6)
            #### if we click on the PLAY button ####
            if click:
                countdown()  ## CALLING COUNTDOWN FUNCTION TO START OUR GAME

        #### if our cursor is on button2 which is INSTRUCTION button
        if button2.collidepoint(x, y):
            ### changing from inactive to active by changing the color from white to red
            pygame.draw.rect(screen, (155, 0, 0), button2, 6)
            #### if we click on the INSTRUCTION button ####
            if click:
                instructionIMG(0, 0)  ### DISPLAYING OUR INSTRUCTION IMAGE BY CALLING IT

        #### if our cursor is on button3 which is ABOUT button
        if button3.collidepoint(x, y):
            ### changing from inactive to active by changing the color from white to red
            pygame.draw.rect(screen, (155, 0, 0), button3, 6)
            #### if we click on the ABOUT button ####
            if click:
                aboutIMG(0, 0)  ### DISPLAYING OUR ABOUT IMAGE BY CALLING IT

        ###### checking for mouse click event
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


###### Countdown ######
def countdown():
    font2 = pygame.font.Font("freesansbold.ttf", 85)
    countdownBacground = pygame.image.load("bg.png")
    three = font2.render("3", True, (187, 30, 16))
    two = font2.render("2", True, (255, 255, 0))
    one = font2.render("1", True, (51, 165, 50))
    go = font2.render("GO!!!", True, (0, 255, 0))

    ##### displaying blank background #####
    screen.blit(countdownBacground, (0, 0))
    pygame.display.update()

    ###### Displaying  three (3) ######
    screen.blit(three, (350, 250))
    pygame.display.update()
    time.sleep(1)

    ##### displaying blank background #####
    screen.blit(countdownBacground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    ###### Displaying  two (2) ######
    screen.blit(two, (350, 250))
    pygame.display.update()
    time.sleep(1)

    ##### displaying blank background #####
    screen.blit(countdownBacground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    ###### Displaying  one (1) ######
    screen.blit(one, (350, 250))
    pygame.display.update()
    time.sleep(1)

    ##### displaying blank background #####
    screen.blit(countdownBacground, (0, 0))
    pygame.display.update()
    time.sleep(1)

    ###### Displaying  Go!!! ######
    screen.blit(go, (300, 250))
    pygame.display.update()
    time.sleep(1)
    gameloop()  # calling the gamloop so that our game can start after the countdown
    pygame.display.update()


# defining our gameloop function
def gameloop():
    ####### music #######
    pygame.mixer.music.load("BackgroundMusic.mp3")
    pygame.mixer.music.play()
    ###### sound effect for collision ######
    crash_sound = pygame.mixer.Sound("car_crash.wav")

    ####### scoring part ######
    score_value = 0
    font1 = pygame.font.Font("freesansbold.ttf", 25)

    def show_score(x, y):
        score = font1.render("SCORE: " + str(score_value), True, (255, 0, 0))
        screen.blit(score, (x, y))

    # highscore part
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    def show_highscore(x, y):
        Hiscore_text = font1.render("HISCORE :" + str(highscore), True, (255, 0, 0))
        screen.blit(Hiscore_text, (x, y))
        pygame.display.update()

    ###### creating our game over function #######

    def gameover():
        gameoverImg = pygame.image.load("gameover.png")
        run = True
        while run:
            screen.blit(gameoverImg, (0, 0))
            time.sleep(0.5)
            show_score(330, 400)
            time.sleep(0.5)
            show_highscore(330, 450)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        countdown()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    # setting background image
    bg = pygame.image.load("bg.png")

    # setting our player
    maincar = pygame.image.load("main car.png")
    maincarX = 350
    maincarY = 495
    maincarX_change = 0
    maincarY_change = 0

    # other cars
    car1 = pygame.image.load("car 1.png")
    car1X = random.randint(178, 490)
    car1Y = 100
    car1Ychange = 10
    car2 = pygame.image.load("car 2.png")
    car2X = random.randint(178, 490)
    car2Y = 100
    car2Ychange = 10

    car3 = pygame.image.load("car 3.png")
    car3X = random.randint(178, 490)
    car3Y = 100
    car3Ychange = 10

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

                # checking if any key has been pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    maincarX_change += 5

                if event.key == pygame.K_LEFT:
                    maincarX_change -= 5

                if event.key == pygame.K_UP:
                    maincarY_change -= 5

                if event.key == pygame.K_DOWN:
                    maincarY_change += 5

                # checking if key has been lifted up
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    maincarX_change = 0

                if event.key == pygame.K_LEFT:
                    maincarX_change = 0

                if event.key == pygame.K_UP:
                    maincarY_change = 0

                if event.key == pygame.K_DOWN:
                    maincarY_change = 0

        # setting boundary for our main car
        if maincarX < 178:
            maincarX = 178
        if maincarX > 490:
            maincarX = 490

        if maincarY < 0:
            maincarY = 0
        if maincarY > 495:
            maincarY = 495

        # CHANGING COLOR WITH RGB VALUE, RGB = RED, GREEN, BLUE
        screen.fill((0, 0, 0))

        # displaying the background image
        screen.blit(bg, (0, 0))

        # displaying our main car
        screen.blit(maincar, (maincarX, maincarY))

        # displaing other cars
        screen.blit(car1, (car1X, car1Y))
        screen.blit(car2, (car2X, car2Y))
        screen.blit(car3, (car3X, car3Y))
        # calling our show_score function
        show_score(570, 280)
        # calling show_hiscore function
        show_highscore(0, 0)

        # updating the values
        maincarX += maincarX_change
        maincarY += maincarY_change

        # movement of the enemies
        car1Y += car1Ychange
        car2Y += car2Ychange
        car3Y += car3Ychange
        # moving enemies infinitely
        if car1Y > 670:
            car1Y = -100
            car1X = random.randint(178, 490)
            score_value += 1
        if car2Y > 670:
            car2Y = -150
            car2X = random.randint(178, 490)
            score_value += 1
        if car3Y > 670:
            car3Y = -200
            car3X = random.randint(178, 490)
            score_value += 1

        # checking if highscore has been created
        if score_value > int(highscore):
            highscore = score_value

        # DETECTING COLLISIONS BETWEEN THE CARS

        # getting distance between our main car and car1
        def iscollision(car1X, car1Y, maincarX, maincarY):
            distance = math.sqrt(
                math.pow(car1X - maincarX, 2) + math.pow(car1Y - maincarY, 2)
            )

            # checking if distance is smaller than 50 after then collision will occur

            if distance < 50:
                return True
            else:
                return False

        # getting distance between our main car and car2
        def iscollision(car2X, car2Y, maincarX, maincarY):
            distance = math.sqrt(
                math.pow(car2X - maincarX, 2) + math.pow(car2Y - maincarY, 2)
            )

            # checking if distance is smaller than 50 after then collision will occur
            if distance < 50:
                return True
            else:
                return False

        # getting distance between our main car and car3
        def iscollision(car3X, car3Y, maincarX, maincarY):
            distance = math.sqrt(
                math.pow(car3X - maincarX, 2) + math.pow(car3Y - maincarY, 2)
            )

            # checking if distance is smaller then 50 after then collision will occur
            if distance < 50:
                return True
            else:
                return False

        ##### giving collision a variable #####

        # collision between maincar and car1
        coll1 = iscollision(car1X, car1Y, maincarX, maincarY)

        # collision between maincar and car2
        coll2 = iscollision(car2X, car2Y, maincarX, maincarY)

        # collision between maincar and car3
        coll3 = iscollision(car3X, car3Y, maincarX, maincarY)

        # if coll1 occur
        if coll1:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
            ###### calling our game over function #######
            time.sleep(1)
            gameover()

        # if coll2 occur
        if coll2:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
            ###### calling our game over function #######
            time.sleep(1)
            gameover()

        # if coll3 occur
        if coll3:
            car1Ychange = 0
            car2Ychange = 0
            car3Ychange = 0
            car1Y = 0
            car2Y = 0
            car3Y = 0
            maincarX_change = 0
            maincarY_change = 0
            pygame.mixer.music.stop()
            crash_sound.play()
            ###### calling our game over function #######
            time.sleep(1)
            gameover()

        if car1Ychange == 0 and car2Ychange == 0 and car3Ychange == 0:
            pass

        # writing to our highscore.txt file
        with open("highscore.txt", "w") as f:
            f.write(str(highscore))

        pygame.display.update()


introscreen()
