from utils import draw_maze, generate_random_maze
from ai_helper import find_shortest_path

def main():
    """
    Main function to execute the maze game with extended features.
    """
    # Generate a random maze
    maze, start, end = generate_random_maze(5, 5)  # 5x5 random maze
    player_pos = start

    print("Welcome to the Extended Maze Game!")
    print("Navigate through the maze to reach the end marked as 'E'.")
    print("Controls: 'up', 'down', 'left', 'right'.")
    print("Type 'hint' for AI suggested path.\n")

    # Game loop
    while player_pos != end:
        # Clear screen for better readability
        print("\033[H\033[J", end="")  # ANSI escape sequences to clear the screen
        draw_maze(maze, player_pos)   # Display the current maze

        # Get player move
        move = input("Enter your move (up, down, left, right, hint): ").strip().lower()

        # Handle "hint" for AI-suggested path
        if move == "hint":
            path = find_shortest_path(maze, player_pos, end)
            if path:
                print("AI Suggested Path:", path)
            else:
                print("No valid path found by AI.")
            input("Press Enter to continue...")
            continue

        # Calculate movement direction
        dx, dy = 0, 0
        if move == "up":
            dx, dy = -1, 0
        elif move == "down":
            dx, dy = 1, 0
        elif move == "left":
            dx, dy = 0, -1
        elif move == "right":
            dx, dy = 0, 1
        else:
            print("Invalid input. Please try again.\n")
            input("Press Enter to continue...")
            continue

        # Validate and update player position
        nx, ny = player_pos[0] + dx, player_pos[1] + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] != 1:
            player_pos = (nx, ny)
        else:
            print("You hit a wall! Try a different direction.\n")
            input("Press Enter to continue...")

    # Game completion message
    print("\033[H\033[J", end="")  # Clear the screen
    draw_maze(maze, player_pos)
    print("Congratulations! You have reached the end of the maze!")


if __name__ == "__main__":
    main()