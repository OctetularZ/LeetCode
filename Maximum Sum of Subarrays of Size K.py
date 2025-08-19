from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int):
        start = 0
        current_sum = 0
        maximum_sum = 0

        for end in range(len(nums)):
            current_sum += nums[end]

            if (end - start + 1) == k:
                maximum_sum = max(maximum_sum, current_sum)
                current_sum -= nums[start]
                start += 1
        
        return maximum_sum


# Sliding window
# Store accumulator, set to 0 initially
# Store maximum sum, set to 0 initially
# Two pointers, one for start of window and second for end of window
# Use for loop, on each iteration add to accumulator
# If len(window) is equal to k, subtract left most element from accumulator, Increase start by 1 then if total greater than maximum sum, then update maximum sum to be equal to new total
