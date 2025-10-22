# Definition of a ListNode
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  
# Linked List tail will have a next of 'None' (unless there is a cycle) indicating the end of a linked list


# Traverse linked list
# Set current to head
# While current is not None meaning it is not the end of the linked list, set current to next ListNode
# Time - O(n): Each node is visited, Space - O(1): Use 1 pointer regardless of size
def findLength(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length


# Deleting node from linked list
# If the head is the target, Return the next node.
# Set two pointers, prev and current
# While not at end of list, if we reach target node, set prev node.next to current nodes.next
# If not, set previous to current node, then set current node to the next node
# Time - O(n): Same reason as above, Space - O(1) - Using 2 pointers regardless of size
def deleteNode(head, target):
    if head.val == target:
        return head.next
    
    prev = None
    curr = head
    
    while curr:
        if curr.val == target:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
    
    return head


# Fast and Slow pointers
# Two pointers, Both start at head of linked list
# When the fast pointer reaches the end, the slow pointer will be at the middle node
# Fast pointer always advances by two nodes
# Slow pointer always advances by one node
# Return slow = middle node
# This will return the second node in the middle out of the two, if there are even nodes.
# Time - O(n): Pointers iterate through each node once, Space - O(1): Two pointers are used regardless of length of list
# Same concept works for finding a cycle in a linked list
def fastAndSlow(head):
    fast = head
    slow = head
    while fast and fast.next: # This checks for both even and odd number of nodes. If there are even nodes (fast = None), it'll reach end faster than if odd number of nodes (fast.next = None). Covers both conditions.
        fast = fast.next.next
        slow = slow.next
    return slow


# Reversing a Linked List
# Uses 3 pointers - previous, current, and next
# To reverse: store current nodes next -> Set current.next to point to previous node -> Update previous node to current node -> Set current node to next node that we stored
# Time - O(n): Pointers iterate through each node once, Space - O(1): Three pointers are used regardless of length of list
def reverse(head):
    prev = None # prev is set to 0 so head points to None making it the tail
    current = head
    while current:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
    return prev # Last node = New head of list


# Merging two linked lists
# How to sort two sorted linked lists
# Get the linked list with the smaller head, then go up 1 on that list as we don't need to compare the first value anymore
# Compare each node, add the smaller one to the end of the current then make current to the next node (the one just added). That way current will always be the last added node.
# Time - O(n + m): Go through each node of two separate linked lists, Space - O(1) - Same amount of space regardless of size as we're not making new nodes
def merge_lists(l1, l2):
    if not l1: return l2
    if not l2: return l1

    if l1.val < l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next
    
    current = head # Initialise a tail, this will represent the last node of merged linked list
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2 # One of the lists will have one or more nodes left, this adds that final node to the end
    return head # Returns l1 or l2, whichever one the smaller one was. As that'll be the start of a sorted array.


# Dummy nodes
# Creating a new node which isn't part of the final list but acts like the start of a new list where we can add elements to it
# Return dummy.next at the end (as dummy isn't part of the list)
def merge_two_lists(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
