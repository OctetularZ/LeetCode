from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0

        for num in hash_set:
            if (
                    num - 1) not in hash_set:  # Checks if num is beginning of sequence. Avoids unncessary work. 1, 2, 3, 4 - yes, 2, 3, 4 - no, as 2 is not start of sequence.
                length = 1
                while (num + length) in hash_set:
                    length += 1
                longest = max(longest, length)

        return longest
