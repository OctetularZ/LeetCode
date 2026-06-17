from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums_freq = Counter(nums)
        res = []
        n = len(nums)

        for key in nums_freq:
            if nums_freq[key] > (n / 3):
                res.append(key)

        return res