from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        list_map = {}
        for i in nums1:
            if i in list_map:
                list_map[i] += 1
            else:
                list_map[i] = 1
        
        for j in nums2:
            if j in list_map and list_map[j] != 0:
                intersection.append(j)
                list_map[j] -= 1
        
        return intersection
        
        

# Store one array in a hashmap
# Loop through second array and lookup current number in hashmap, if present, add to new array
