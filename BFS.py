# BFS
# - BFS is a level-by-level traversal algorithm
# - Starts at a node in a tree or graph-like data structure and processes all nodes at the current level before moving to the nodes at the next level.
# - BFS uses a queue to keep track of the nodes it needs to visit
# - BFS is better for questions that ask something about the nodes at each level

# deque is a doubly-linked list so operations are faster compared to a normal list
# We use deque - Supports pop(0) in O(1) time with popleft() and we can use .append() as normal
# Even supports O(1) time for both ends as it supports FIFO and LIFO
# Even has appendleft() in O(1) time!!!
# Has a .rotate as well to rotate the array at a certain index

from collections import deque

def bfs(root):
    if not root:
        return []

    result = [] # Storing nodes, not really part of code but just for display purposes
    queue = deque([root]) # Initialise queue with root

    while queue: # While queue is not empty
        curr_node = queue.popleft() # Remove node from queue
        result.append(curr_node.val)
        
        if curr_node.left:
            queue.append(curr_node.left) # Add to queue if there is a left
        if curr_node.right:
            queue.append(curr_node.right) # Add to queue if there is a right
          
        # This way, for every node, we add it's left then it's right. So we always visit the left then right node next (the level)
        # Therefore fulfilling the condition for BFS

    return result


# DESCRIPTION - Given a binary tree, return the level-order traversal of its nodes' values. (i.e., from left to right, level by level).

def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        # number of nodes at the current level
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            curr = queue.popleft()
            current_level.append(curr.val)
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        # IMPORTANT
        # we have finished processing all nodes at the current level
        result.append(current_level)
        
    return result
