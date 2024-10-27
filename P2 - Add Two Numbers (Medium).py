# Mine

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_node_array = [l1.val]
        l1_index_counter = 1
        l1_value = l1
        while l1_value != None:
            l1_node_array.append((l1_value.next))
            try:
                l1_value = l1_node_array[l1_index_counter]
            except:
                break
            l1_index_counter += 1
        l1_node_array.pop()
        l1_numb_arr = []
        for l1_numb in l1_node_array:
            if type(l1_numb) == int:
                l1_numb_arr.append(l1_numb)
            else:
                l1_numb_arr.append(l1_numb.val)

        l2_node_array = [l2.val]
        l2_index_counter = 1
        l2_value = l2
        while l2_value != None:
            l2_node_array.append((l2_value.next))
            try:
                l2_value = l2_node_array[l2_index_counter]
            except:
                break
            l2_index_counter += 1
        l2_node_array.pop()
        l2_numb_arr = []
        for l2_numb in l2_node_array:
            if type(l2_numb) == int:
                l2_numb_arr.append(l2_numb)
            else:
                l2_numb_arr.append(l2_numb.val)

        l1_numb_arr.reverse()
        l1_str = ''
        for number in l1_numb_arr:
            l1_str += str(number)
        l2_numb_arr.reverse()
        l2_str = ''
        for number in l2_numb_arr:
            l2_str += str(number)
        total = int(l1_str) + int(l2_str)
        total_arr = []
        for letter in str(total):
            total_arr.append(letter)
        total_arr.reverse()
        total_arr_int = []
        for letter in total_arr:
            total_arr_int.append(int(letter))
        final_LN = []
        for number in total_arr_int:
            final_LN.append(ListNode(number, None))
        index_counter = len(final_LN)
        for index in range(0, index_counter):
            try:
                final_LN[index].next = final_LN[index + 1]
            except IndexError:
                final_LN[index].next = None
        return final_LN[0]


# Model Answer

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
