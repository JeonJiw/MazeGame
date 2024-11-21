from typing import List, Tuple
import random
from colorama import Fore, Style

def draw_maze(maze: List[List[int]], player_pos: Tuple[int, int]) -> None:
    """
    Draws the maze with the current player position using colors.

    :param maze: 2D list representing the maze
    :param player_pos: Tuple of player's current position (row, column)
    """
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                print(Fore.GREEN + "P" + Style.RESET_ALL, end=" ")  # Player's position
            elif cell == 1:
                print(Fore.RED + "#" + Style.RESET_ALL, end=" ")  # Wall
            elif cell == 0:
                print(".", end=" ")  # Open path
            elif cell == "S":
                print(Fore.YELLOW + "S" + Style.RESET_ALL, end=" ")  # Start
            elif cell == "E":
                print(Fore.CYAN + "E" + Style.RESET_ALL, end=" ")  # End
        print()
    print()

def generate_random_maze(rows: int, cols: int) -> Tuple[List[List[int]], Tuple[int, int], Tuple[int, int]]:
    """
    Generates a random maze with start and end points.

    :param rows: Number of rows in the maze
    :param cols: Number of columns in the maze
    :return: A tuple containing the maze, start position, and end position
    """
    maze = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

    # Ensure start and end points are open
    start = (0, 0)
    end = (rows - 1, cols - 1)
    maze[start[0]][start[1]] = "S"
    maze[end[0]][end[1]] = "E"

    # Clear a basic path for simplicity
    for i in range(rows):
        for j in range(cols):
            if (i, j) in [start, end]:
                continue
            if random.random() > 0.7:  # Randomly set some paths to open
                maze[i][j] = 0
    return maze, start, end