from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def find_length(self, head):
        length = 0

        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        return length


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head

        length = self.find_length(head)
        target = length - n + 1
        
        if length == 1:
            return None

        if length == n:
            return head.next

        curr = head
        i = 1

        while curr:
            if i == target:
                prev.next = curr.next
                print(i)
                break
            prev = curr
            curr = curr.next
            i += 1
        
        return head
        

# Use a counter, i = 1
# Find length of list, target = length of list - n + 1
# Traverse through linked list
# On each traversal, check if target = i, if so remove the node, otherwise add one to counter
