from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]):
        if not intervals:
            return [newInterval]

        intervals.append(newInterval)
        sortedIntervals = sorted(intervals, key=lambda x: x[0])

        intervalAdded = []

        for interval in sortedIntervals:
            if not intervalAdded or interval[0] > intervalAdded[-1][1]:
                intervalAdded.append(interval)
            else:
                intervalAdded[-1][1] = max(interval[1], intervalAdded[-1][1])
            print(intervalAdded)

        return intervalAdded
        



# If intervals is empty, return newInterval
# Add new interval to intervals
# Sort intervals by start time
# For loop through intervals, starting from second interval
# If current interval start time is less than previous interval end time, this is an overlap
# So set previous interval's end time to max(between both intervals)
# Add to new array
# Return new array
