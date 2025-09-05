from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != "O":
                return
            
            board[r][c] = "S"

            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        
        for r in range(len(board)):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][len(board[0]) - 1]:
                dfs(r, len(board[0]) - 1)
        
        for c in range(len(board[0])):
            if board[0][c] == "O":
                dfs(0, c)
            if board[len(board) - 1][c] == "O":
                dfs(len(board) - 1, c)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        
        return board

# Check for every region starting from the border of the board
# Mark those regions with an "S"
# Go through entire board and change the "S"s for "O"s and the "O"s for "X"s
