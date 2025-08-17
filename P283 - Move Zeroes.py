from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] == 0:
                rem = nums.pop(left)
                nums.append(rem)
                right -= 1
            else:
                left += 1
