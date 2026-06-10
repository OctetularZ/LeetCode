from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_k = [x for x, _ in count.most_common(k)]

        return most_k
