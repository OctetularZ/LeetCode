def rotate(nums, k):
    counter = len(nums) - 1
    pop_index = len(nums) - 1
    while counter >= len(nums) - k:
        removed_item = nums.pop(pop_index)
        nums.insert(0, removed_item)
        counter -= 1
    return nums


lst = [1, 2, 3, 4, 5, 6, 7]
print(rotate(lst, 3))

# while start_index <= len(nums):
#     nums.pop(start_index)
#     start_index -= 1  # Try use sets and remove a whole subset of new_lst in nums
