from typing import List, Optional


class Solution:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        target_arrays = []

        def dfs(node, arr=[]):
            nonlocal target_arrays
            if node is None:
                return
            
            if node.left is None and node.right is None:
                arr.append(node.val)
                total = sum(arr)
                if total == targetSum:
                    target_arrays.append(arr.copy())
                arr.pop()
                return
            
            arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)
            arr.pop()
        
        dfs(root)
        return target_arrays

# Use a global array to store each subarray which adds to target
# Each path taken will need it's own array
# An array will be passed down, as we go down, append current nodes value to array
# Use a helper function to pass down an array
# At each leaf node, check if sum of array is equal to target, if so, add to global array

# Important Lesson - When you append a list to a list, it is copied by reference. So if you modify that list you appended after, it'll be affected in the final array
# I had no idea but that's why I do these. To learn.
# Advice - Instead of appending list directly (i.e. list1.append(list2), use list.copy() (i.e. list1.append(list2.copy() )))
