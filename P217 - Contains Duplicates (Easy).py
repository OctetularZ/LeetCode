from collections import Counter
from typing import List


def containsDuplicate(self, nums: List[int]) -> bool:
    return not (len(nums) == len(set(nums)))
