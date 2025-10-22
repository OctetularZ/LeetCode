# Use arrays as stacks
stack = []

# Append to add to top of stack
stack.append(1)

# Pop to remove fom top of stack
stack.pop()

# Stacks are effective for managing the ordering of nested sequences, as the order in which we must process the sequences matches the order in which they are popped from the stack.
# Example - {(())} - Sequence of open bracket must equal closing brackets sequence


# Monotonic stack - A special stack which is sorted in ascending or descending order

# Decreasing
def nextGreaterElement(nums):
  n = len(nums)
  result = [-1] * n
  stack = []

  for i in range(n):
    while stack and nums[i] > nums[stack[-1]]:
      index = stack.pop()
      result[index] = nums[i]
    stack.append(i)

  return result


# Keep adding to stack until current value is greater than current value on stack and stack isn't empty
# If so, then keep removing from stack and adding to indexed array until it is no longer true (stack is empty or current value ins't larger than value on stack)

# Increasing
def nextSmallerElement(nums):
  n = len(nums)
  result = [-1] * n
  stack = []

  for i in range(n):
    while stack and nums[i] < nums[stack[-1]]:
      index = stack.pop()
      result[index] = nums[i]
    stack.append(i)

  return result