from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        current_sum = 0
        max_sum = 0
        window_dict = {}

        for end in range(len(nums)):
            window_dict[nums[end]] = window_dict.get(nums[end], 0) + 1
            current_sum += nums[end]

            if (end - start + 1) == k:
                if len(window_dict) == k:
                    max_sum = max(max_sum, current_sum)

                current_sum -= nums[start]
                window_dict[nums[start]] -= 1
                if window_dict[nums[start]] == 0:
                    del window_dict[nums[start]]
                start += 1

        return max_sum

                

# Sliding window approach
# Two pointers, one for start of window (initially 0), second for end of window
# If array is valid, check if it's distinct, len(window_dict) == k, check max sum, slide window by 1
