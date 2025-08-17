from typing import List


class Solution:
    def threeSum(self, nums: List[int]):
        triplets = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[left], nums[right], nums[i]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return triplets

# Two pointers (left from start, right from end)
# For Loop through len(arr) - 2 (as right will start from the end so we'll always see end of array)
# If i > 0 and i and the value behind i are the same, skip that loop (Skip duplicates)
# Set left = i + 1, right = len(arr) - 1
# While left < right, find total
# If total < 0 - left += 1, total > 0 - right -= 1,
# If total == 0, while arr[left] == arr[left + 1] and left < right, left += 1
# Same for right to make sure duplicates are skipped
