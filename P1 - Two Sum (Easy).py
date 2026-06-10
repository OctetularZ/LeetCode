from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_arr = {}

        for i in range(len(nums)):
            hash_arr[nums[i]] = i

        for i in range(len(nums)):
            find = target - nums[i]
            if find in hash_arr and hash_arr[find] != i:
                return [i, hash_arr[find]]
