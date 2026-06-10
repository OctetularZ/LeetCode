import heapq
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        for i in range(len(nums) - 1, -1, -1):
            nums[i] = -heapq.heappop(max_heap)

        return nums
