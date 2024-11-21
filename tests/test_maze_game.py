import unittest
from maze_game import main

class TestMazeGame(unittest.TestCase):
    def test_game_run(self):
        """
        Test if the game runs without errors.
        """
        try:
            main()  # Simulate running the game
        except Exception as e:
            self.fail(f"Game execution failed with error: {e}")