from typing import List


# Brute Force
def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)

    # Brute Force - O(n**2) - For loop and the "in" operator

    # for i in range(n + 1):
    #     if i not in nums:
    #         return i


    # More efficient method - 0ms - Beats 100% - O(n)
    total = sum(nums)
    range_sum = 0
    for i in range(1, n + 1):
        range_sum += i
    return range_sum - total

    # Optimal Solution - Math equation for first 'n' natural numbers

    # expected = n * (n + 1) // 2
    # return expected - sum(nums)