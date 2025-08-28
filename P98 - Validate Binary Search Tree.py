from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_, max_):
            if node is None:
                return True
            
            if node.val <= min_ or node.val >= max_:
                return False
            
            return dfs(node.left, min_, node.val) and dfs(node.right, node.val, max_)

        
        return dfs(root, -float('inf'), float('inf'))
        


# We need a way to pass down the min and max values
# We need to do know whether the left and right subtrees are binary search trees, 
# return values are true or false
# Base case - Node is None so we return True as it's a valid search Tree as there are no children
