# Maze Game

A text-based maze game where the player navigates through a randomly generated maze to reach the endpoint marked as `E`. The game offers intuitive controls to move up, down, left, or right, and includes an AI feature to suggest the shortest path to the goal.

---

## Game Description

In this game, you are placed in a 5x5 maze. The goal is to navigate from the starting point (`S`) to the endpoint (`E`) while avoiding walls (`#`). You can request AI assistance to find the shortest path if you get stuck.

---

## How to Play

1. **Controls**:

   - Use the following commands to move:
     - `up`: Move up.
     - `down`: Move down.
     - `left`: Move left.
     - `right`: Move right.
   - Type `hint` to get an AI-suggested path to the endpoint.
   - Type `q` to quit the game.

2. **Objective**:
   - Reach the endpoint `E` while avoiding walls `#`.

---

## Example Gameplay

### **Maze Example**

```plaintext
S . # . .
# # . . .
. . . # .
. # # . .
. . . . E
```

### **Player Input and Response**

- Initial Maze:

  ```plaintext
  S . # . .
  # # . . .
  . . . # .
  . # # . .
  . . . . E
  ```

- Player types `down`:

  ```plaintext
  . . # . .
  S # . . .
  . . . # .
  . # # . .
  . . . . E
  ```

- Player types `hint`:

  ```plaintext
  AI Suggested Path: [(0, 0), (1, 0), (2, 0), (3, 1), (4, 2), (4, 3), (4, 4)]
  ```

- Player reaches the endpoint:

  ```plaintext
  . . # . .
  # # . . .
  . . . # .
  . # # . .
  . . . . P

  Congratulations! You have reached the end of the maze!
  ```

---

## How to Run the Project

### Prerequisites

- Python 3.6 or higher
- Recommended: A virtual environment for dependency management

### Installation Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/<your-username>/MazeGame.git
   cd MazeGame
   ```

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the game**:
   ```bash
   python maze_game.py
   ```

---

## Notes

- Use a terminal that supports ANSI escape codes for the best experience (e.g., macOS/Linux terminal or Windows Terminal).
- The AI hint feature uses a simple algorithm to calculate the shortest path and may not account for certain edge cases in complex mazes.

---
