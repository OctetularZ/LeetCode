import heapq

# Heaps
# We use lists to represent heaps in Python
# The list has a special property: list[0] must be the smallest or largest element in the array
# Min-heap, start with smallest, max-heap, start with largest
# We can also think of a heap as a binary tree where elements correspond to a level-order traversal (At each level, read from left to right)
# Min-heap - Each node has a value which is less than or equal to the values of both it's children (not combined)
# Max-heap - Each node has a value which is greater than or equal to the values of both it's children (not combined)
# Any tree/list which follows these properties is a heap
# Values are added from left to right
# Heaps are also completed binary trees so all levels of the tree are filled except the last level which is filled from left to right
# Height of a heap = O(log n) where "n" is the number of elements in the heap

# Parent-child relationship (where i = index)
# Left child = (2 x i) + 1
# Right child = (2 x i) + 2
# Parent = (i - 1) // 2 (floor division)

# Heap operations (disc. "root" - last element)
# push(element) - Add a new element to heap
# 1) Add to new element to next available position in last level of tree
# 2) Bubble up - Compare new element with parent and keep moving up tree until new element is greater than it's parent or until it reaches the root of the heap
# Time complexity - O(log n) - "n" is number of nodes - Each swap is O(1) and we're only going up the levels of the tree


# pop() - Remove the root element from heap
# Removes smallest element in heap (the root) so when it's removed, it must be replaced by the new smallest element in the heap
# 1) Remove root element and replace with last element in the heap
# 2) Bubble down - Compare root with children, if root is greater than any of the children, swap with the smaller child. Repeat until new root is greater than both of its children
# Time complexity - O(log n) - "n" is number of nodes - Each swap is O(1) and we're only going up the levels of the tree


# peek() - Get the root element without removing it
# Returns the minimum value in the heap (the root)
# Time complexity - O(1)

# heapify([elements]) - Converts an array to a heap in-place
# 1) Starting with first non-leaf node (the parent of the last node), compare node with it's children
# 2) If node greater than any of it's children, swap with smaller child
# 3) Move to next non-leaf node and repeat process until the root is reached
# Time complexity - O(n)

# Python has the module: heapq
# Makes handling heaps much easier


# Python Heapq module

# Min-heap

arr = [3, 1, 4, 1, 5, 9, 2]

# convert array into a heap in-place. O(n)
heapq.heapify(arr)

# push 0 to the heap. O(log n)
heapq.heappush(arr, 0)

# peek the min element = 0. O(1)
arr[0]

# pop and return the min element = 0. O(log n)
min_element = heapq.heappop(arr)

# peek the new min element = 1. O(1)
arr[0]


#----------

# Max-heap

# negate the values in the array
negated_arr = [-x for x in arr]

# convert array into a min-heap
heapq.heapify(negated_arr) 

# push 11 to the heap by negating it
heapq.heappush(negated_arr, -11)

# peek root of heap = -11
negated_arr[0]

# pop and return the max element = -11
max_element = -heapq.heappop(negated_arr)

# peek the new max element = 9
negated_arr[0]

#------------

# Heap tuples
# Ordered based on first element in tuple by default
# If first element is equal, second element is compared and so on.

arr = [(3, 1), (1, 5), (4, 2), (1, 9), (5, 3), (9, 4), (2, 6)]
heapq.heapify(arr)

# pop and return the min element = (1, 5)
min_element = heapq.heappop(arr)

# peek the new min element = (1, 9)
arr[0]

# push (1, 7) to the heap, which is smaller than (1, 9)
heapq.heappush(arr, (1, 7))

# peek the min element = (1, 7)
arr[0]


#-----------

# Use case - Top-K largest elements in an array
# 1) Store first 3 elements of array in a min-heap. This'll represent the 3 largest elements we've seen so far with smallest number as the root.
# 2) Iterate through remaining elements in array
# 3) If current element larger than root of heap, pop from heap then add current element
# 4) Otherwise, repeat for remaining elements
