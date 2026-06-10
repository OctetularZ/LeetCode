from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(path, total, index):
            if total == target:
                res.append(path[:])
                return

            if total > target or index == len(candidates):
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(path, total + candidates[i], i + 1)
                path.pop()

        backtrack([], 0, 0)
        return res

# Backtracking
# Parameters -> (path, total, index)
#
