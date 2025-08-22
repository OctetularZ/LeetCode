from typing import List


class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        days = 0
        stack = []
        result = [0] * n

        for i in range(n):
           
            while stack and temps[i] > temps[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        
        return result


# n = length of array
# Initialise result array, [0] * n
# days = 0
# stack = []

# For loop through temps
# While stack isnt empty and current temp is more than top of stack:
# Remove index from stack and update result array at index to counter
# Else add 1 to counter
