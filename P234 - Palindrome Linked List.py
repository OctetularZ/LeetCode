from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def find_mid(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def reverse_list(self, head):
        prev = None
        curr = head

        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        return prev


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        middle = self.find_mid(head)
        reversed_half = self.reverse_list(middle)
        
        p1 = reversed_half
        p2 = head
        while p1:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return True

        

# Use fast and slow pointers to find middle node
# Reverse second half of linked list
# Compare both linked lists, if all equal, return True, otherwise, return False
