def pair_finder(arr, k):
  arr_hash = {}
  for i in range(len(arr)):
    arr_hash[arr[i]] = i

  pairs = []
  for i in range(len(arr)):
    if arr[i] - k in arr_hash:
        pairs.append([arr[i] - k, arr[i]])
    
  return pairs


#Test
arr = [1, 7, 5, 9, 2, 12, 3]
print(pair_finder(arr, 2))
