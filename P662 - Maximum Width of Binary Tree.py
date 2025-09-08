# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # enqueue the root node with position 0
        queue = deque([(root, 0)])
        max_ = 0

        while queue:
            level_size = len(queue)

            # leftPos is the position of the leftmost node at the current level
            _, leftPos = queue[0]
            rightPos = -1

            for i in range(level_size):
                node, pos = queue.popleft()

                # update rightPos to the position of the rightmost node
                # when we reach the last node in the level
                if i == level_size - 1:
                    rightPos = pos

                # add the children to the queue with their positions
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))
            
            # rightPos - leftPos + 1 is the width of the current level 
            max_ = max(max_, rightPos - leftPos + 1)

        return max_
