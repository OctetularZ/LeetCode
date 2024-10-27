def removeElement(nums):
    current_index = 0
    for i in range(len(nums)):
        if current_index + 1 >= len(nums):
            break
        if nums[current_index] == nums[current_index + 1]:
            nums.pop(current_index)
            current_index -= 1
        current_index += 1

    k = len(nums)
    return k


print(removeElement([1, 1, 2]))