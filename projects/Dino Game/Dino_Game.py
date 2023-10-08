import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Set the title and icon of the window
pygame.display.set_caption("Chrome Dinosaur Game")
icon = pygame.image.load("dino.png") # Load the dino icon from a file
pygame.display.set_icon(icon)

# Create a dino object with an image, a position and a velocity
dino = pygame.sprite.Sprite()
dino.image = pygame.image.load("dino.png") # Load the dino image from a file
dino.rect = dino.image.get_rect() # Get the rectangle of the image
dino.rect.x = 100 # Set the x position of the dino
dino.rect.y = 400 # Set the y position of the dino
dino.vel_y = 0 # Set the initial y velocity of the dino

# Create a cactus object with an image, a position and a velocity
cactus = pygame.sprite.Sprite()
cactus.image = pygame.image.load("cactus.png") # Load the cactus image from a file
cactus.rect = cactus.image.get_rect() # Get the rectangle of the image
cactus.rect.x = 800 # Set the x position of the cactus
cactus.rect.y = 400 # Set the y position of the cactus
cactus.vel_x = -5 # Set the x velocity of the cactus

# Create a group to store all the sprites
sprites = pygame.sprite.Group()
sprites.add(dino) # Add the dino to the group
sprites.add(cactus) # Add the cactus to the group

# Create a variable to store the game state
running = True

# Create a loop to run the game logic
while running:
    # Fill the screen with white color
    screen.fill((255, 255, 255))

    # Draw all the sprites on the screen
    sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Handle the events
    for event in pygame.event.get():
        # If the user clicks the close button, exit the game
        if event.type == pygame.QUIT:
            running = False
        
        # If the user presses a key, check which key it is
        if event.type == pygame.KEYDOWN:
            # If the user presses space or up arrow, make the dino jump
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                # If the dino is on the ground, set its y velocity to -15
                if dino.rect.y == 400:
                    dino.vel_y = -15
    
    # Update the position and velocity of the dino
    dino.rect.y += dino.vel_y # Add the y velocity to the y position
    dino.vel_y += 1 # Add gravity to the y velocity

    # If the dino goes below the ground, set its position and velocity to zero
    if dino.rect.y > 400:
        dino.rect.y = 400
        dino.vel_y = 0
    
    # Update the position and velocity of the cactus
    cactus.rect.x += cactus.vel_x # Add the x velocity to the x position

    # If the cactus goes out of the screen, reset its position and velocity
    if cactus.rect.x < -100:
        cactus.rect.x = 800
        cactus.vel_x -= 1 # Increase the speed of the cactus
    
    # Check for collision between the dino and the cactus
    if pygame.sprite.collide_rect(dino, cactus):
        # If there is a collision, stop the game and print "Game Over"
        running = False
        print("Game Over")

pygame.quit()
