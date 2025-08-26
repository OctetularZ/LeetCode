import heapq
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for i in range(len(arr)):
            distance = abs(arr[i] - x)

            if len(heap) < k:
                heapq.heappush(heap, [-distance, i])
            elif distance < abs(heap[0][0]) or (distance == abs(heap[0][0]) and arr[i] < arr[heap[0][1]]):
                    heapq.heappop(heap)
                    heapq.heappush(heap, [-distance, i])
        
        closest_elements = [arr[x[1]] for x in heap]
        closest_elements.sort()
        return closest_elements
        

# Use max heap (will store [distance, index])
# Iterate through arr, calculate distance from x
# If len(heap) is less than k, add [distance, index] to heap
# else, if distance is less than root of heap, pop from heap and add new element to heap
# If distance is equal but a is less than b, pop from heap and add new element to heap
# Return array of elements with index of arr[element[1]]
