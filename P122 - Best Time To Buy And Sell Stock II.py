from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        max_profit = 0

        left, right = 0, 0

        while left < len(prices) and right < len(prices):
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)

            if right < len(prices) - 1 and prices[right] > prices[right + 1]:
                res += max_profit
                max_profit = 0
                left = right = right + 1
                continue

            right += 1

        return res + max_profit

# What has worked from small tests sizes, I doubt it'll work with all test cases:
# Use two pointers (both begin from the start)
# If right is smaller than left, move left to right position
# Otherwise, keep moving right and re-evaluating max profit
# When value just after right position is smaller, move left pointer and right pointer to that position.

# It actually worked :))
# There were two ways to get the next smaller element in the if condition.
# It's either I make both pointers equal so the if condition can trigger in the next loop with a continue to skip the right += 1 at the end
# Or Use a while loop to keep moving the left pointer forward until we reach a smaller element (argueably cleaner/better)
