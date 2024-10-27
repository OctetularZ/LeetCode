class Solution(object):
    def twoSum(self, nums, target):
        lst_range = len(nums)
        iterations = 1
        for index_one in range(0, lst_range):
            for index_two in range(iterations, lst_range):
                first_number = nums[index_one]
                second_number = nums[index_two]
                total = first_number + second_number
                if total == target:
                    if index_two == index_one:
                        for index_two_recheck in range(index_two, lst_range):
                            if index_two_recheck == second_number:
                                return [index_one, index_two_recheck]
                            else:
                                pass
                    else:
                        return [index_one, index_two]
                else:
                    pass
            iterations += 1


# Nums (array of integers)
# Target (target integer)
# One solution from an array
# Return indices (index)
