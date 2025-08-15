# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def make_list(self, vals):
        head = ListNode(vals[0])
        vals.pop(0)
        curr = head

        for numb in vals:
            prev = curr
            curr = ListNode(numb)
            prev.next = curr

        return head

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        if not head.next:
            return head

        curr = head.next
        vals = []
        total = 0

        while curr:
            if curr.val == 0:
                vals.append(total)
                total = 0
                curr = curr.next
            elif curr.val > 0:
                prev = curr.val
                curr.val += total
                total += prev
                curr = curr.next

        return self.make_list(vals)


# Optimal solution

# class Solution:
#     def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return head
#
#         if not head.next:
#             return head
#
#         curr = head.next
#         curr2 = curr
#
#         while curr2:
#             total = 0
#             while curr2.val != 0:
#                 total += curr2.val
#                 curr2 = curr2.next
#
#             curr.val = total
#             curr2 = curr2.next
#             curr.next = curr2
#             curr = curr.next
#
#         return (head.next)