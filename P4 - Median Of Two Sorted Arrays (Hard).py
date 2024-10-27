def findMedianSortedArrays(nums1, nums2):
    merged_array = []
    for number in nums1:
        merged_array.append(number)
    for number in nums2:
        merged_array.append(number)
    merged_array.sort()
    median = ((len(merged_array) + 1) / 2) - 1
    median_as_string = str(median)
    if median_as_string.endswith('5'):
        median_start = median_as_string[:-2]
        median_start = int(median_start)
        median_end = median_start + 1
        final_median = (merged_array[median_start] + merged_array[median_end]) / 2
    else:
        median = int(median)
        final_median = merged_array[median]
    return float(final_median)


arr1 = [1, 2]
arr2 = [3, 4]
print(findMedianSortedArrays(arr1, arr2))
