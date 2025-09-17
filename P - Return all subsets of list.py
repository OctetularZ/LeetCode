# Given a set of distinct integers, nums, return all possible subsets (the power set), without duplicates.

def solution(nums):
  if not nums:
    return []
  
  def backtrack(path, index):
    if index == len(nums):
      result.append(path.copy())
      return
    
    path.append(nums[index])
    backtrack(path, index + 1)

    path.pop()
    backtrack(path, index + 1)
    
  
  result = []
  backtrack([], 0)
  return result

nums = [1, 2, 3]
print(solution(nums))


# Pass path and index