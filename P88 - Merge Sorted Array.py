from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for numb in nums2:
            nums1[m] = numb
            m += 1
        
        nums1.sort()
