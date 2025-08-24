from typing import List


class Solution:
    def time_taken(self, piles, rate):
        time = 0
        for i in range(len(piles)):
            time += (piles[i] + rate - 1) // rate
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            if self.time_taken(piles, mid) > h:
                left = mid + 1
            else:
                right = mid
        
        return left
