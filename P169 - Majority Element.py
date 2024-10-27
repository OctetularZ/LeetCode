def majorityElement(nums):
    nums_dict = {}
    keys = []
    for i in nums:
        if nums_dict.get(i) is None:
            nums_dict[i] = nums.count(i)
            keys.append(i)
    for key in keys:
        if nums_dict[key] > (len(nums) / 2):
            return key


lst = [3, 2, 3]
print(majorityElement(lst))
