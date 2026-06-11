from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        res = []

        def backtrack(path, start):
            if len(path) == k:
                res.append(path[:])
                return

            if len(path) > k:
                return

            for i in range(start + 1, n + 1):
                path.append(i)
                backtrack(path, i)
                path.pop()

        for i in range(1, n + 1):
            backtrack([i], i)
        return res

# Backtracking
# Cannot use the same number twice (unique combinations)
# Parameters - (path, start) - path is the current path, and start is what number to start from when choosing next numbers to add to path.
# Cont. Essentially creating a range from start to n
# Base case - if len(path) == k
# k is always less than or equal to n so we don't have to worry about that aspect
