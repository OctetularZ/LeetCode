from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        sortedInterval = sorted(intervals, key=lambda x: x[0])
        
        merged = []

        for interval in sortedInterval:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged


# Edge case -intervals = 0, return [newInterval]
# Added new interval to intervals
# Create a new array which has the intervals array but sorted
# if new intervals array is empty or there is no overlap with interval in new interval array, add interval to new intervals
# Otherwise, if there is an interval, add to new interval array by updating the end time of the previous interval with the max between both intervals
