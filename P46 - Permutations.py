from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, visited, index):
            if len(path) == len(nums) or index >= len(nums):
                res.append(path[:])
                return

            if len(path) > len(nums):
                return

            visited.add(index)

            for i in range(len(nums)):
                if i in visited:
                    continue
                path.append(nums[i])
                backtrack(path, visited, i)
                path.pop()

            visited.remove(index)

        for i in range(len(nums)):
            backtrack([nums[i]], set(), i)
        return res

# Backtracking
# parameters - (path, index)
# Base case - len(path) == len(nums)
# For uniqueness, don't use same number twice
