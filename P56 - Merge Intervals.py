from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort(key = lambda x: x[0])
        merged = []

        for i in range(len(intervals)):
            if not merged or intervals[i][0] > merged[-1][1]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
        
        return merged


# Sort intervals by start time
# Initialise new array to store merged and non-merged intervals
# For loop through intervals, if start time of current interval is in merged intervals is less than or equal to the previous interval's end time, it is an overlap, so merge it then add to merged array
# Merge - Add new array to merged where start time is previous start time and end time is max between both end times
