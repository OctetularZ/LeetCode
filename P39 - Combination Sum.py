from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(path, total, index):
            if total > target:
                return

            if total == target:
                res.append(path[:])
                return

            for idx in range(index, len(candidates)):
                path.append(candidates[idx])
                backtrack(path, total + candidates[idx], idx)
                path.pop()

        backtrack([], 0, 0)

        return res

# Thought process:
# Backtracking to get combinations
# We already have our base case from question - If total of combination == target
# Pruning - If combination > target: return
# All elements can be chosen, any number of times
# Backtracking function parameters - path, index
# Path will be added to result array if valid, index to keep track and make sure we don't duplicate answers
# Incrementation of index will only happen in the outside for loop. Inside for loop always takes whole array/subarray
