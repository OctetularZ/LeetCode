from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        right_intervals = []
        start_times = []
        for i in range(len(intervals)):
            start_times.append([intervals[i][0], i])
        start_times.sort(key=lambda x: x[0])
        
        for j in intervals:
            left, right = 0, len(start_times) - 1
            ll = -1

            while left <= right:
                mid = (left + right) // 2

                if start_times[mid][0] >= j[1]:
                    ll = start_times[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
        
            right_intervals.append(ll)

        return right_intervals
        


# Make a new array with each intervals start time and it's index
# Loop through intervals array and with each end time, find a start time which is more than or equal to the end from the new array
# Keep binary searching until you get the lowest possible start time
# When you find the smallest possible start time, add index to a index array
# Return index array
