from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                temp = nums[l]
                nums[l] = nums[i]
                nums[i] = temp
                l += 1
            elif nums[i] == 2:
                temp = nums[r]
                nums[r] = nums[i]
                nums[i] = temp
                r -= 1
                i -= 1
            i += 1
        return nums
