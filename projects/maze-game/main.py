import random

def generate_maze(size, player, goal):
    """Generates a maze grid."""
    maze = [['_' for _ in range(size)] for _ in range(size)]
    maze[player[0]][player[1]] = 'P'  # Player position
    maze[goal[0]][goal[1]] = 'G'     # Goal position
    count = {x:0 for x in range(size)}
    for _ in range(size * 2):        # Add obstacles
        x,y = random.randint(0,size-1),random.randint(0,size-1)
        if [x,y]!=player and [x,y]!=goal and count[x]<size-1:
            maze[x][y] = '#'
    return maze

def display_maze(maze):
    """Prints the maze."""
    for row in maze:
        print(' '.join(row))
    print()

def move_player(maze, player, direction):
    """Moves the player in the specified direction."""
    x, y = player
    maze[x][y] = '_'  # Clear current position
    if direction == 'w' and x > 0: x -= 1   # Move up
    elif direction == 's' and x < len(maze) - 1: x += 1  # Move down
    elif direction == 'a' and y > 0: y -= 1  # Move left
    elif direction == 'd' and y < len(maze[0]) - 1: y += 1  # Move right
    
    if maze[x][y] != '#':  # Check for obstacles
        player[0], player[1] = x, y
    maze[player[0]][player[1]] = 'P'  # Update position
    return player

def check_win(player, goal):
    """Checks if the player reached the goal."""
    return player == goal

def play_game():
    """Main game logic."""
    size = 6  # Maze size
    player = [0, 0]  # Starting position
    goal = [size - 1, size - 1]  # Goal position
    print(goal)
    maze = generate_maze(size, player, goal)
    
    print("Welcome to the Maze Game!")
    print("Navigate using 'w', 'a', 's', 'd' (up, left, down, right). Reach the goal (G) to win!")
    display_maze(maze)
    
    while True:
        move = input("Enter your move (w/a/s/d): ").lower()
        if move not in ['w', 'a', 's', 'd']:
            print("Invalid move! Use 'w', 'a', 's', or 'd'.")
            continue
        
        player = move_player(maze, player, move)
        display_maze(maze)
        
        if check_win(player, goal):
            print("Congratulations! You've reached the goal!")
            break

# Start the game
play_game()
