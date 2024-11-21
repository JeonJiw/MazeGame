from collections import deque
from typing import List, Tuple

def find_shortest_path(maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    Uses BFS to find the shortest path from start to end in the maze.

    :param maze: 2D list representing the maze
    :param start: Starting position in the maze
    :param end: Ending position in the maze
    :return: List of positions representing the shortest path
    """
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Reverse the path to get start-to-end order

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != 1 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = current

    return []  # No valid path found