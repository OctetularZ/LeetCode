from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        rows, cols = len(board), len(board[0])

        def backtrack(r, c, index):
            if index == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            found = False

            for dr, dc in directions:
                if backtrack(r + dr, c + dc, index + 1) == True:
                    found = True

            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True

        return False

# DFS
# Pass indexes for grid and index for word
# Backtracking - We can't automatically rule out visited cells in grid
# In word search, you can have a different starting point but use the same letters you've already visited
# This is where backtracking comes in. You need to temporarily mark cells are visited then when you backtrack. un-visit them.
# If cell is not equal to current index in word, return early with False
