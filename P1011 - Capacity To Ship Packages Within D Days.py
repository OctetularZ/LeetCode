from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_weight = max(weights)
        total = sum(weights)
        min_capacity = total

        left, right = max_weight, total

        while left <= right:
            max_capacity = (left + right) // 2
            current_days = 1
            current_capacity = 0

            for i in weights:
                if current_capacity + i > max_capacity:
                    current_days += 1
                    current_capacity = 0

                current_capacity += i

            if current_days > days:
                left = max_capacity + 1
            else:
                min_capacity = min(min_capacity, max_capacity)
                right = max_capacity - 1

        return min_capacity

# Least weight capacity - The smallest number we can use so the weights can be shipped in 'days' days
# So if we output 10 - We can only load a maximum of 10 per day (using the weights in order)
# Get the maximum weight from weights
# Start binary search between 0 and max of weights
# How to check number of days required by current capacity (O(n)):
# Use a for loop and current capacity counter
# If current capacity more than or equal to max capacity:
# Add 1 to current days counter
# Then minus max capacity from current capacity
# Restore min(days, current days counter)
# If current days counter more than days, search right side of range
# Otherwise search left side if current days less than days
# We have to find a capacity which gives us exactly days

# O(n log (n))