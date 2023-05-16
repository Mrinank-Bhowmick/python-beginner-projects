import pygame
import random


class Display:
    pygame.init()
    windows = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Space Shooter")
    clock = pygame.time.Clock()

    background = pygame.image.load("background.png")
    font = pygame.font.Font("SHPinscher-Regular.otf", 35)

    spaceship = pygame.image.load("spaceship.png")
    enemy_spaceship = pygame.image.load("enemy spaceship.png")
    enemy_missile_craft = pygame.image.load("missile spaceship.png")
    laser = pygame.image.load("bullet.png")
    enemy_laser = pygame.image.load("enemy laser.png")
    missile = pygame.image.load("missile.png")


class Text:
    def __init__(self, text: str, size: int):
        self.text = text
        self.size = size
        self.selected = False

    def display(self):
        # Change the color if selected
        color = (255, 0, 0) if self.selected else (255, 255, 255)
        font = pygame.font.Font("SHPinscher-Regular.otf", self.size)
        return font.render(self.text, True, color)


class Menu:
    def __init__(self):
        self.text_list = []
        self.selected = 1

    def text(self):
        # Text on the main menu
        text_list = ["Main Menu", "Start", "Exit"]
        # Size for the text
        size_list = [70, 40, 40]

        # Create text class and append to list
        self.text_list = [
            Text(text_list[i], size_list[i]) for i in range(len(text_list))
        ]
        # Select the first option
        self.text_list[1].selected = True

    def controls(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                self.select(1)
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.select(2)

    def select(self, code: int):
        # Go down the list
        if code == 1:
            if self.selected == 1:
                self.selected = 2
                self.text_list[1].selected = False
            else:
                self.selected -= 1
                self.text_list[self.selected + 1].selected = False

        # Go up the list
        if code == 2:
            if self.selected == 2:
                self.selected = 1
                self.text_list[2].selected = False
            else:
                self.selected += 1
                self.text_list[self.selected - 1].selected = False

        self.text_list[self.selected].selected = True

    def buttons_function(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Start button
                if self.selected == 1:
                    Start().execute()
                # Exit button
                if self.selected == 2:
                    exit()

    def objects(self):
        spacing = 50
        # Display the background
        Display().windows.blit(Display().background, (0, 0))
        # Display the text
        for text in self.text_list:
            Display().windows.blit(
                text.display(),
                (
                    (Display().windows.get_width() - text.display().get_width()) / 2,
                    spacing,
                ),
            )
            spacing += 100

    def execute(self):
        self.text()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                self.controls(event)
                self.buttons_function(event)

            self.objects()

            pygame.display.flip()


class GameOver:
    def __init__(self):
        self.text_list = []
        self.selected = 0

    def text(self, code: int):
        options = ["Yes", "No"]
        if code == 1:
            return Text("Game Over", 90).display()
        if code == 2:
            return Text("Play Again?", 30).display()
        if code == 3:
            self.text_list = [Text(text, 25) for text in options]
            self.text_list[0].selected = True

    def objects(self):
        # Background
        Display().windows.blit(Display().background, (0, 0))
        # Text
        Display().windows.blit(
            self.text(1),
            ((Display().windows.get_width() - self.text(1).get_width()) / 2, 70),
        )
        Display().windows.blit(
            self.text(2),
            ((Display().windows.get_width() - self.text(2).get_width()) / 2, 200),
        )
        # Options
        for text in self.text_list:
            if text == self.text_list[0]:
                ops = (
                    Display().windows.get_width() - text.display().get_width()
                ) / 2 - 50
            else:
                ops = (
                    Display().windows.get_width() - text.display().get_width()
                ) / 2 + 50

            Display().windows.blit(text.display(), (ops, 250))

    def controls(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.select(1)
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                self.select(2)

    def select(self, code: int):
        if code == 1:
            if self.selected == 1:
                self.selected = 0
                self.text_list[1].selected = False
            else:
                self.selected += 1
                self.text_list[self.selected - 1].selected = False

        if code == 2:
            if self.selected == 0:
                self.selected = 1
                self.text_list[0].selected = False
            else:
                self.selected -= 1
                self.text_list[self.selected + 1].selected = False

        self.text_list[self.selected].selected = True

    def buttons_func(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Start button
                if self.selected == 0:
                    Start().execute()
                # Exit button
                if self.selected == 1:
                    exit()

    def execute(self):
        self.text(3)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                self.controls(event)
                self.buttons_func(event)

            self.objects()

            pygame.display.flip()


class Enemies:
    def __init__(self):
        # Place the enemies at random
        self.x = random.randint(700, 1000)
        self.y = random.randint(
            0,
            Display().windows.get_height() - Display().enemy_spaceship.get_height() + 1,
        )
        # Randomly select between two types of enemies
        self.type = random.choice([1, 2])
        # List for the location of the lasers/missiles
        self.bullets_list = []
        self.alive = True

    def collision_box(self):
        return pygame.Rect(
            (self.x, self.y),
            (
                Display().enemy_spaceship.get_width(),
                Display().enemy_spaceship.get_height(),
            ),
        )

    def firing(self):
        # Append the location of lasers/missiles
        self.bullets_list.append([self.x, self.y])


class Objects:
    def __init__(self):
        # Initial location of the spaceship
        self.x = 40
        self.y = (Display().windows.get_height() - Display.spaceship.get_width()) / 2
        # List of lasers
        self.laser_list = []
        # List of enemies
        self.enemies_list = []
        # How many initial enemies there should be
        self.enemy_count = 3
        # Background location
        self.background_list = [[0, 0], [1800, 0]]
        self.score = 0
        # Condition
        self.condition = 10

    def objects(self):
        # Background
        Display().windows.fill((0, 0, 0))
        # Stars Background
        self.background()
        # Collision Box
        self.collision_box()
        # Space_Ship
        Display().windows.blit(Display().spaceship, (self.x, self.y))
        # Laser
        self.fire_laser()
        # Enemies
        self.enemies_movement()
        # Score
        self.score_board()

    def collision_box(self):
        return pygame.Rect(
            (self.x, self.y),
            (Display().spaceship.get_width(), Display().spaceship.get_height()),
        )

    def background(self):
        for location in self.background_list:
            # Display the background
            Display().windows.blit(Display().background, (location[0], location[1]))
            # Change the x location of the background to give the illusion of movement
            location[0] -= 2

            if location[0] + Display().background.get_width() <= 0:
                # Resets the location of the background if it's offscreen
                index = self.background_list.index(location)
                self.background_list[index][0] = (
                    self.background_list[index - 1][0] + 1800
                )

    def add_enemies(self):
        # Adds enemy if score is more or equals than the limit
        if self.score >= self.condition:
            self.enemy_count += 1
            # Increase the limit
            self.condition += 10

    def score_board(self):
        # Display the scoreboard
        score_board = Display().font.render(
            f"Score: {self.score}", True, (255, 255, 255)
        )
        Display().windows.blit(score_board, (10, 0))

    def insert_laser(self):
        # Insert the location of a laser based on the position of the spaceship
        self.laser_list.append([self.x + Display().spaceship.get_width(), self.y])

    def fire_laser(self):
        for location in self.laser_list:
            # Makes a pygame.Rect object to make a collision box
            rect = pygame.Rect(
                (location[0], location[1] + 15),
                (Display().laser.get_width(), Display().laser.get_height() - 30),
            )
            # Display the laser
            Display().windows.blit(Display().laser, (location[0], location[1]))

            # Checks whether or not the laser hits an enemy
            self.laser_hit(rect, location)
            # Removes the laser if it's offscreen
            if (
                location[0] + Display().laser.get_width()
                >= Display().windows.get_width()
                and location in self.laser_list
            ):
                self.laser_list.remove(location)
            # Changes the location of the laser to move it
            location[0] += 5

    def laser_hit(self, rect: pygame.Rect, laser: list):
        for enemies in self.enemies_list:
            # Calls the collision functions
            collision = rect.colliderect(enemies.collision_box())
            # If the enemies got hit and is alive
            if collision and enemies.alive:
                # Removes the laser
                if laser in self.laser_list:
                    self.laser_list.remove(laser)
                # Removes the enemies
                self.reset_enemies(enemies, False)
                self.score += 1

    def reset_enemies(self, enemies: Enemies, condition: bool):
        enemies.alive = False
        # Remove the enemies
        if condition:
            self.enemies_list.remove(enemies)
            self.enemy_count -= 1
        # Enemies will still be on the list but no removed so that the laser/missile will still be visible
        if not condition:
            self.enemy_count += 1

    def place_enemies(self):
        for i in range(self.enemy_count):
            # Place the enemies within the limit
            if len(self.enemies_list) < self.enemy_count:
                self.enemies_list.append(Enemies())

    def enemies_movement(self):
        for enemies in self.enemies_list:
            # Spawn enemies
            if enemies.type == 1 and enemies.alive:
                Display().windows.blit(
                    Display().enemy_spaceship, (enemies.x, enemies.y)
                )
            if enemies.type == 2 and enemies.alive:
                Display().windows.blit(
                    Display().enemy_missile_craft, (enemies.x, enemies.y)
                )

            # Moves the enemy if not in limit
            if enemies.x >= 550:
                enemies.x -= 2
            # Fires when it's in position
            else:
                self.enemy_laser(enemies)

    def enemy_laser(self, enemy: Enemies):
        # Fires a laser/missile
        if len(enemy.bullets_list) < 1 and enemy.alive:
            enemy.firing()
        self.enemy_firing(enemy)

    def enemy_firing(self, enemy: Enemies):
        # Enemy type that fires laser
        if enemy.type == 1:
            self.enemy_type1_firing(enemy)
        # Enemy type that fires missile
        elif enemy.type == 2:
            self.enemy_type2_firing(enemy)

    def enemy_type1_firing(self, enemy: Enemies):
        for laser in enemy.bullets_list:
            # Display the laser
            Display().windows.blit(
                Display().enemy_laser,
                (laser[0] - Display().enemy_spaceship.get_width(), laser[1] + 28),
            )
            # Creates the collision box
            collision = pygame.Rect(
                (laser[0] - Display().enemy_spaceship.get_width(), laser[1] + 28),
                (Display().enemy_laser.get_width(), Display().enemy_laser.get_height()),
            )

            # Removes the laser if out of screen
            if laser[0] + Display().enemy_laser.get_width() <= 0:
                enemy.bullets_list.remove(laser)
                # Checks if enemy is hit
                self.enemy_hit(enemy)

            # Checks if the laser hit the player
            self.player_hit(collision)
            laser[0] -= 5

    def enemy_type2_firing(self, enemy: Enemies):
        for missile in enemy.bullets_list:
            # Display the missile
            Display().windows.blit(
                Display().missile,
                (missile[0] - Display().enemy_missile_craft.get_width(), missile[1]),
            )
            # Creates the collision box
            collision = pygame.Rect(
                (missile[0] - 80, missile[1]),
                (Display().missile.get_width(), Display().missile.get_height()),
            )

            # Removes the missile if out of screen
            if missile[0] + Display().missile.get_width() <= 0:
                enemy.bullets_list.remove(missile)
                # Checks if enemy is hit
                self.enemy_hit(enemy)

            # Checks if the laser hit the player
            self.player_hit(collision)
            missile[0] -= 2

            # Makes the missile follow the player
            if missile[0] > Display().windows.get_width() / 2:
                if self.y < missile[1]:
                    missile[1] -= 2
                if self.y > missile[1]:
                    missile[1] += 2

    def enemy_hit(self, enemy: Enemies):
        if not enemy.alive:
            self.reset_enemies(enemy, True)

    def player_hit(self, collision: pygame.Rect):
        # Checks if the player has been hit or not
        hit = collision.colliderect(self.collision_box())
        # Ends the game
        if hit:
            GameOver().execute()


class Start:
    def __init__(self):
        self.object = Objects()
        self.enemies = Enemies()
        self.up = False
        self.down = False

    def controls(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.up = True
            if event.key == pygame.K_s:
                self.down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.up = False
            if event.key == pygame.K_s:
                self.down = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.object.insert_laser()

    def movements(self):
        if self.up and self.object.y >= 0:
            self.object.y -= 5
        if (
            self.down
            and self.object.y + Display().spaceship.get_height()
            <= Display().windows.get_height()
        ):
            self.object.y += 5

    def execute(self):
        while True:
            self.object.place_enemies()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                self.controls(event)

            self.movements()
            self.object.objects()
            self.object.add_enemies()

            pygame.display.flip()
            Display().clock.tick(60)


Menu().execute()
