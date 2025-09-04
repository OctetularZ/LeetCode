from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return
        
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        change = image[sr][sc]

        def dfs(r, c):
            if (r, c) in visited:
                return
            
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            
            if image[r][c] == change:
                image[r][c] = color
            else:
                return
            
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return

        dfs(sr, sc)
        return image

# DFS
# Created a global set to store visited pixels
# Colour of image[sr][sc] needs to be stored globally
# Array of directions to store all possible directions from any given pixel
# Use a helper function to pass down row and column
# On each DFS iteration (at each pixel), check if:
    # Check if pixel is in visited
    # Check if pixel is in range
    # If pixel is equal to global colour (image[sr][sc]):
        # Change value of [r, c](current node) to new colour
    # Otherwise:
        # Skip (return)

# Repeat for each neighbour of the pixel