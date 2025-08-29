from typing import Optional


class Solution:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        counter = 0

        def dfs(node):
            nonlocal counter
            if node is None:
                return 0
            
            if node.left is None and node.right is None:
                return 1
            
            left = dfs(node.left)
            right = dfs(node.right)

            counter = max(counter, left + right)

            return max(left, right) + 1

        dfs(root)
        return counter


# Use a global counter, add 1 for every node we go up
# If leaf node, add 1 to counter
# If node is None, return 0
# On each iteration, return sum of left and right counters
# update global counter to max of both the sum of left and right subtrees
