def two_pointers(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return True
        
        if total < target:
            left += 1
        else:
            right -= 1
    
    return False


# For searching an array for a pair (or more) of items in an array that meet a certain criteria. Array must be ordered.
