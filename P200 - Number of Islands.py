from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return
        
        islands = 0
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if (r, c) in visited:
                return
            
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            
            visited.add((r, c))

            if grid[r][c] == "1":
                for dr, dc in directions:
                    dfs(r + dr, c + dc)
            else:
                return


        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    if (r, c) not in visited:
                        islands += 1
                    dfs(r, c)

        return islands

# DFS
# If list is empty, return
# Store islands count {globally}
# Store a set of visited nodes, (r, c) {globally}
# directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] {globally}
# Nested for loops to get each node in the grid
# At each node:
    # Check if node is in visited
    # Check if node is within the boundary
    # Add (r, c) to visited
    # If node is equal to 1:
        # Add 1 to island count
        # Run a dfs until we find the find all land next to that land and all the neighbouring lands
    # Else return
