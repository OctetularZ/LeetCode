def removeElement(nums, val):
    current_index = 0
    for i in range(len(nums)):
        if nums[current_index] == val:
            nums.remove(val)
            current_index -= 1
        current_index += 1
    print(nums)

    k = len(nums)
    return k


print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))