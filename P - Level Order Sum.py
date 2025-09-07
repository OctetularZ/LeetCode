class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque


class Solution:
    def level_order_sum(self, root: TreeNode):
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            sum = 0
            level_length = len(queue)

            for _ in range(level_length):
                curr = queue.popleft()
                sum += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            result.append(sum)
        
        return result
