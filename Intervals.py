# Overlapping intervals
# This function sorts each interval in an array of intervals, 
# And returns True or False whether there's an overlap between any interval or not.

def canAttendMeetings(intervals):
    if not intervals:
        return True # Intervals is an empty array return True
    
    intervals.sort(key=lambda x: x[0]) # Sorts array based on the lowest start time - [1]
    
    for i in range(1, len(intervals)): # For each interval in intervals (starting from second interval):
        if intervals[i][0] < intervals[i-1][1]: # Check if start time of interval, is less than the end time of the previous interval
            return False # If so, return False - There are overlaps
    i
    return True # If no overlaps, return True


# Merging intervals - If there are overlaps, they can be merged.
# Set end time of previous interval = max(end times of either interval)
# Function for merging intervals

def mergeIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0]) # Sort array like we did in previous function
    merged = [] # List that will contain updated intervals
        
    for interval in sortedIntervals: # Loop through intervals
        if not merged or interval[0] > merged[-1][1]: # If merged is empty or if current interval start time is more than previous interval end time:
            merged.append(interval) # Add to merged array - Don't do merge witha anything
        else:
            merged[-1][1] = max(interval[1], merged[-1][1]) # Merge intervals - Set end time of previous interval to max(between end time of current and previous)

    return merged # Return merged array


# Code for merging intervals
prev_interval[1] = max(prev_interval[1], interval[1])


# Sorting by end time
# Why: For example, finding maximum number of non-overlapping intervals, if an interval starts early but ends late, we cannot add the next interval until that interval is finish, even if the rest don't overlap.
# Sorting by end time allows us to bypass this issue, as we can get the interval that ends first, making room for the other intervals.
intervals.sort(key=lambda x: x[1]) # - Same thing as sorting but just change key to [1] - End time



# Non-Overlapping intervals
# Sort by end times then iterate over intervals, keeping a count of all intervals that overlap with the previous interval in the non-overlapping set
# Function:

def nonOverlappingIntervals(intervals):
    if not intervals:
        return 0 # If intervals is empty, return 0 as there are 0 overlaps

    intervals.sort(key=lambda x: x[1]) # Sorting by end time
    end = intervals[0][1] # Get first end time
    count = 1 # Count start at 1, as even if they're all overlapping, you'd have to remove at least 1 to get rid of overlap

    for i in range(1, len(intervals)): # Start loop from second interval
        if intervals[i][0] >= end: # Check if current interval start time overlaps with previous interval end time
            end = intervals[i][1] # Set previous to current
            count += 1 # Add 1 to count if there is no overlap

    return len(intervals) - count # Return len(intervals) - count = number of intervals which need to be removed
