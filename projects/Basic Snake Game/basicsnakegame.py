import random
import os
import msvcrt
import time

# Constants
WIDTH, HEIGHT = 20, 10
SNAKE_CHAR = 'O'
FOOD_CHAR = 'X'

# Initial game state
snake = [(WIDTH // 2, HEIGHT // 2)]
food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
direction = (1, 0)

# Function to display the game board
def display_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    board = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for x, y in snake:
        board[y][x] = SNAKE_CHAR

    x, y = food
    board[y][x] = FOOD_CHAR

    for row in board:
        print(' '.join(row))

# Function to get user input
def get_user_input():
    while True:
        if msvcrt.kbhit():
            key = ord(msvcrt.getch())
            if key == 224:
                key = ord(msvcrt.getch())
            if key == 72:  # Up arrow
                return (0, -1)
            elif key == 80:  # Down arrow
                return (0, 1)
            elif key == 75:  # Left arrow
                return (-1, 0)
            elif key == 77:  # Right arrow
                return (1, 0)

# Main game loop
while True:
    display_board()
    direction = get_user_input()

    # Update the snake's position
    head_x, head_y = snake[-1]
    new_head = (head_x + direction[0], head_y + direction[1])

    if new_head == food:
        snake.append(new_head)
        food = (random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
    else:
        snake.append(new_head)
        snake.pop(0)

    # Check for collision with the walls
    if (new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT):
        print("Game Over!")
        break

    # Check for self-collision
    if new_head in snake[:-1]:
        print("Game Over!")
        break

    time.sleep(0.2)
