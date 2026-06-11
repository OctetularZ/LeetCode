from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        if not nums:
            return res

        def backtrack(path, visited, index):
            if len(path) == len(nums):
                res.append(path[:])
                return

            if len(path) > len(nums) or index >= len(nums):
                return

            if nums[index] in visited:
                return

            res.append(path[:])

            for i in range(index + 1, len(nums)):
                if i > index + 1 and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(path, visited, i)
                path.pop()

        visited = set()
        for i in range(len(nums)):
            backtrack([nums[i]], visited, i)
            visited.add(nums[i])

        return res

# Base case - len(path) == len(nums) or index > len(nums)
# Backtrack params - (path, index)