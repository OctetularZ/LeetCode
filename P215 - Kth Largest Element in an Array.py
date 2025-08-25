import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counter = 0
        neg_nums = [-x for x in nums]
        heapq.heapify(neg_nums)
        largest_numb = 0
        
        while counter < k:
            largest_numb = -heapq.heappop(neg_nums)
            counter += 1

        return largest_numb


# Use max heap
# Keep popping from heap until you get the kth largest element
# Why? The largest element will always be the root. So keep taking away the largest element k amount of times to get the kth largest element
