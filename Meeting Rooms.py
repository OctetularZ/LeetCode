from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]):
        if not intervals:
            return True
        
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        
        return True
        

# Sort array using start time
# For each interval, after the first, if start time of current is less than end time of previous, return False - there is an overlap
# If not, return True
