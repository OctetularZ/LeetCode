from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if 0 not in nums:
            return len(nums) - 1

        start = 0
        zero_index = None
        max_counter = 0
        counter = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else:
                if zero_index == None:
                    zero_index = i
                else:
                    max_counter = max(max_counter, counter)
                    while start <= zero_index:
                        if nums[start] == 1:
                            counter -= 1
                        start += 1
                    zero_index = i
                    print(zero_index)

        max_counter = max(max_counter, counter)
        return max_counter


# Sliding Window
# Two pointers, one for start of window and other for end of window
# Store zero index = None
# Store max counter, set to 0
# Store counter, set to 0
# For loop through binary nums -
# If current num is 1, add 1 to counter
# If current num is 0 and delete == None, set delete to index of 0 (index = i) and continue, if delete != None, end of sequence, set max counter and keep reducing counter by 1 (if it's a 1, otherwise just increase start by 1 - I think I can just minus zero index) till start of window points to first 1 after first 0 (current zero index + 1)
# Repeat from there
# Return max counter
