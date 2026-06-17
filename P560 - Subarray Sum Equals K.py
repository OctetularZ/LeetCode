from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix_count = {0: 1}
        current_sum = 0

        for i in nums:
            current_sum += i
            diff = current_sum - k

            res += prefix_count.get(diff, 0)

            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return res