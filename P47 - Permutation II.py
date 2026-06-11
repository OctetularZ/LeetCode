from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if i in visited:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and (i - 1) not in visited:
                    continue

                visited.add(i)
                path.append(nums[i])

                backtrack(path)

                path.pop()
                visited.remove(i)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            visited.add(i)
            backtrack([nums[i]])
            visited.remove(i)

        return res
