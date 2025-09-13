from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        fresh_oranges = 0
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0

        while queue and fresh_oranges > 0:
            minutes += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                r, c = curr

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        queue.append((nr, nc))
        
        if fresh_oranges == 0:
            return minutes
        else:
            return -1
