import math
from typing import List
import heapq


# Sorting solution
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: math.sqrt((x[0] - 0)**2 + (x[1] - 0)**2))
        return points[:k]


# Heap solution using a max-heap
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    heapq.heapify(heap)

    for i in range(len(points)):
        x, y = points[i]
        distance = math.sqrt((x) ** 2 + (y) ** 2)

        if len(heap) >= k:
            min_point = heapq.heappop(heap)
            if distance < -min_point[0]:
                heapq.heappush(heap, [-distance, points[i]])
            else:
                heapq.heappush(heap, min_point)
        else:
            heapq.heappush(heap, [-distance, points[i]])

    print(heap)
    res = [point[1] for point in heap]
    return res

# Min-heap
# Each value in min_heap will be sorted by the euclidean distance
# So each value will be a tuple/array with two values, the distance and the coordinates
# Why? We need to return the coordinates not the distance, however distance is important for heap order
