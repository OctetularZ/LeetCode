# Concept
# Two pointers
# One will indicate start of window, second will indicate the end of window
# Keep expanding/moving window as long as criteria is met
# Otherwise, move window to right (static) or move only start pointer by 1 (dynamic/varied-length)
# When moving window, removed old elements (which aren't in window anymore) from sum/dictionary/etc.
# Repeat until condition met (longest substring, longest unique subarray, etc)
# O(n)

# Example - Fruits into basket

# Description:
# Write a function to calculate the maximum number of fruits you can collect from an integer array fruits, where each element represents a type of fruit. You can start collecting fruits from any position in the array, but you must stop once you encounter a third distinct type of fruit. The goal is to find the longest subarray where at most two different types of fruits are collected.
# Example:
# Input: fruits = [3, 3, 2, 1, 2, 1, 0]
# Output: 4
# Explanation: We can pick up 4 fruit from the subarray [2, 1, 2, 1]

def fruit_into_baskets(fruits):
  start = 0 # Set start of window
  state = {} # Store counter for each fruit visited
  max_fruit = 0 # Max fruits which can be visited (read desc)

  for end in range(len(fruits)): # This will signify the end of the window, expand to end of array
    state[fruits[end]] = state.get(fruits[end], 0) + 1 # Get fruit in hashmap and add 1 to it (counter)

    while len(state) > 2: # While there are more than types of fruits in the hashmap
      state[fruits[start]] -= 1 # Reduce left most fruit counter by 1 until you it becomes 0
      if state[fruits[start]] == 0: # When it's 0:
        del state[fruits[start]] # Remove left most fruit from hashmap
      start += 1 # Keep reducing window, till it's valid again. Or in other words, until at least one fruit is removed.

    max_fruit = max(max_fruit, end - start + 1) # Set the maximum fruits which can be visited

  return max_fruit
