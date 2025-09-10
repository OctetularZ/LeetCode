from collections import deque

class Solution:
    def minimum_knight_moves(self, x: int, y: int):
        directions = [(1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1)]

        visited = set([(0, 0)])
        queue = deque([(0, 0)])
        moves = 0

        while queue:
            level_length = len(queue)
            moves += 1
            for _ in range(level_length):
                curr = queue.popleft()
                r, c = curr
                if r == x and c == y:
                    return moves - 1
                for dr, dc in directions:
                    next_r = r + dr
                    next_c = c + dc
                    if next_r >= -200 and next_c >= -200 and next_r < 200 and next_c < 200 and (next_r, next_c) not in visited:
                        queue.append((next_r, next_c))
                        visited.add((next_r, next_c))
                        print((r, c), (next_r, next_c))


# BFS
# On each iteration, add (x + 2, y + 1) and (x + 1, y + 2) and the negative versions of those
# Assumption - It's always possible to reach a solution
# Run BFS until a solution is found
# Intialise a queue with (0, 0)
