from collections import Counter
from typing import List


def containsDuplicate(self, nums: List[int]) -> bool:
    counter = Counter(nums)
    for key in counter:
        if counter[key] > 1:
            return True

    return False
