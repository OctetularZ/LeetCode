from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(node):
            nonlocal total
            if node is None:
                return 0
            
            if node.left is None and node.right is None:
                return node.val
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            total += abs(left - right)

            return node.val + left + right
        
        dfs(root)

        return total
    

# From the left and right subtree, I need the total sum of nodes then I can find the absolute difference of both
# Base case - If there are no nodes to traverse to/ if node is none.
