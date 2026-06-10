from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = 0

        def backtrack(total, index):
            nonlocal res
            if index == len(nums) - 1:
                res += total
                return

            res += total

            for i in range(index + 1, len(nums)):
                backtrack(total ^ nums[i], i)

        for i in range(len(nums)):
            backtrack(nums[i], i)
        return res

# Backtracking (total, index)
# When backtracking again, exclude index we've already used to keep uniqueness of subsets.
# Base case - If index == len(nums) - 1
# Outside for loop, loop through all elements
