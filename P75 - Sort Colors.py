from typing import List


class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[high], arr[i + 1] = arr[i + 1], arr[high]
        return i + 1

    def sortColors(self, nums: List[int], low=0, high=None) -> None:
        if high is None:
            high = len(nums) - 1

        if low < high:
            pivot_index = self.partition(nums, low, high)
            self.sortColors(nums, low, pivot_index - 1)
            self.sortColors(nums, pivot_index + 1, high)
        