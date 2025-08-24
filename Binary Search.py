# Binary Search
# Split array in two, check if middle is target, 
# Get lower half or higher half of array depending on if target is low or higher than middle value
# Repeat until target is found
def binary_search(nums, target):
  left = 0
  right = len(nums) - 1

  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    if nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1

  return -1