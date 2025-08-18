# Find pairs [a, b] in array where the difference between [a, b] == k

def binary_search(arr, target):
  left, right = 0, len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
      return True
    
    if arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  
  return False

def find_pairs(arr, k):
  pairs = []
  arr.sort()
  
  for i in range(len(arr)):
    m = binary_search(arr, arr[i] - k)

    if m == True:
      pairs.append([arr[i] - k, arr[i]])
  
  return pairs


# Loop through array once
# For each element in the array, binary search for a - k or b - k
# If found, it is a pair, add to pairs

#Test
arr = [1, 7, 5, 9, 2, 12, 3]
print(find_pairs(arr, 2))