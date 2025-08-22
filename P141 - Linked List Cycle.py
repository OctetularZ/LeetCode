# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False

# If head is None - Return False
# Set two pointers, one slow = head and one fast = head.next
# If they are equal, then there is a cycle, otherwise, no cycle
