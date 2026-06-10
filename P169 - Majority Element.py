from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        for [key, value] in count.items():
            if count[key] > len(nums)/2:
                return key
