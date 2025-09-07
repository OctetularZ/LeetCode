# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import List, Optional


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        direction = "left"
        queue = deque([root])

        while queue:
            level_nodes = []
            level_length = len(queue)

            for _ in range(level_length):
                curr = queue.popleft()
                level_nodes.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if direction == "right":
                level_nodes.reverse()
                result.append(level_nodes)
                direction = "left"
            else:
                result.append(level_nodes)
                direction = "right"
            
        return result
    

# Use a variable to control whether we're going left or right
# Initially set to left
# If right, we reverse list of current level nodes before adding to a result array
# If left, we just add normally
