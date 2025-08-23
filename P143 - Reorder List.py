from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_mid(self, head):
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

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return head

        middle = self.get_mid(head)
        p2 = self.reverse_list(middle)

        p1 = head

        while p2.next:
            p1.next, p1 = p2, p1.next # Set first node next to p2, then set p1 to the next node (now so whatever p1.next was before changing the next, p1 = p1.next, Works from right to left. Right side is evaulated then left side is assigned)
            p2.next, p2 = p1, p2.next # Set second node next to p1, then set p2 to the next node
        
        return head


        
# Don't need to trim list of first, can be done or original list.
# Split linked list in half
# Get second half and reverse it
# Insert reversed link list into first linked list at every 2nd position
# To insert, use a while loop through second list, add from first then second until second list is empty
