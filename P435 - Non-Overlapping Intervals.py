from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        sortedIntervals = sorted(intervals, key=lambda x: x[1])
        prev_interval = sortedIntervals[0]
        count = 1

        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[i][0] >= prev_interval[1]:
                count += 1
                prev_interval = sortedIntervals[i]
        
        return len(sortedIntervals) - count

# [2, 3], [3, 4], [1, 5], [4, 6]
# 

# Sort array by end times
# count = 1 - If there's only one in intervals, then it's a non-overlap
# Count all non-overlaps
# Loop through intervals, if start time of current is more or equal to than end time of previous, then it is a non-overlap, count += 1
# Return len(intervals) - count = number of overlaps
