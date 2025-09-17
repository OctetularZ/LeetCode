from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        def backtrack(path, index):
            if index == len(nums):
                result.append(path.copy())
                return
            
            path.append(nums[index])
            backtrack(path, index + 1)

            path.pop()
            backtrack(path, index + 1)
            
        
        result = []
        backtrack([], 0)
        return result
