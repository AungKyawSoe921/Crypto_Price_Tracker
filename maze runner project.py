# Define the maze
maze = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "P", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", " ", "E", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

# Player's initial position
player_position = [1, 1]


# Function to display the maze
def display_maze(maze):
    for row in maze:
        print("".join(row))
    print()


# Function to move the player
def move_player(direction):
    x, y = player_position
    if direction == 'W':  # Up
        new_position = [x - 1, y]
    elif direction == 'S':  # Down
        new_position = [x + 1, y]
    elif direction == 'A':  # Left
        new_position = [x, y - 1]
    elif direction == 'D':  # Right
        new_position = [x, y + 1]
    else:
        return False

    if maze[new_position[0]][new_position[1]] != "#":
        maze[x][y] = " "
        player_position[0], player_position[1] = new_position
        if maze[new_position[0]][new_position[1]] == "E":
            print("Congratulations! You reached the exit!")
            return True
        maze[new_position[0]][new_position[1]] = "P"

    return False


# Main game loop
game_over = False
while not game_over:
    display_maze(maze)
    move = input("Move (WASD): ").upper()
    if move in ["W", "A", "S", "D"]:
        game_over = move_player(move)
    else:
        print("Invalid move! Use W, A, S, or D.")

print("Game Over")
