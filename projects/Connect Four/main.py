import numpy as np
import pygame
import sys
import math

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
SIZE = (WIDTH, HEIGHT)

# Initialize Pygame
pygame.init()

# Font for winner message (smaller size)
myfont = pygame.font.SysFont("monospace", 50)
winner_font = pygame.font.SysFont("monospace", 30)

# Initialize the game board
def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT))

# Drop piece on the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Check if a column is a valid location
def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

# Get the next available row in a column
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

# Check for a winning move
def winning_move(board, piece):
    # Horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if (
                board[r][c] == piece
                and board[r][c + 1] == piece
                and board[r][c + 2] == piece
                and board[r][c + 3] == piece
            ):
                return True

    # Vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c] == piece
                and board[r + 2][c] == piece
                and board[r + 3][c] == piece
            ):
                return True

    # Diagonal positive slope
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if (
                board[r][c] == piece
                and board[r + 1][c + 1] == piece
                and board[r + 2][c + 2] == piece
                and board[r + 3][c + 3] == piece
            ):
                return True

    # Diagonal negative slope
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if (
                board[r][c] == piece
                and board[r - 1][c + 1] == piece
                and board[r - 2][c + 2] == piece
                and board[r - 3][c + 3] == piece
            ):
                return True
    return False

# Draw the game board
def draw_board(board, screen):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(
                screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE)
            )
            pygame.draw.circle(
                screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS
            )

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(
                    screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS
                )
            elif board[r][c] == 2:
                pygame.draw.circle(
                    screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS
                )
    pygame.display.update()

# Show popup winner message
def show_popup(screen, message):
    popup = pygame.Surface((400, 200))
    popup.fill(WHITE)
    text = winner_font.render(message, True, BLACK)
    popup.blit(text, (50, 70))

    screen.blit(popup, (WIDTH // 2 - 200, HEIGHT // 2 - 100))
    pygame.display.update()

# Main game loop
def main():
    board = create_board()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Connect Four")

    game_over = False
    turn = 0

    draw_board(board, screen)

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                col = int(math.floor(event.pos[0] / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, turn + 1)

                    if winning_move(board, turn + 1):
                        show_popup(screen, f"Player {turn + 1} Wins!")
                        pygame.time.wait(5000)  # Wait for 5 seconds before ending the game
                        game_over = True

                    turn = (turn + 1) % 2
                    draw_board(board, screen)

    pygame.quit()

if __name__ == "__main__":
    main()
