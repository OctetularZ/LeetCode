from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        start = 0
        max_points = 0
        array_sum = sum(cardPoints)
        sub_array_sum = 0

        if k >= len(cardPoints):
            return array_sum
        
        for end in range(len(cardPoints)):
            sub_array_sum += cardPoints[end]
            if (end - start + 1) == len(cardPoints) - k:
                window_sum = array_sum - sub_array_sum
                max_points = max(max_points, window_sum)
                sub_array_sum -= cardPoints[start]
                start += 1

        return max_points



# Sliding Window
# Valid window - When length of window = len(arr) - k
# Sum of window = sum of array - sum of subarray
# Window starts at start of array
# Update max_sum on each window push
# Not a very descriptive algorithm, will update later, a pretty smart way of solving the problem
