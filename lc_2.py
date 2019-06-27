# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(max(len(l1),len(l2)))
# Space: O(max(len(l1),len(l2)))

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        sum_list_head = ListNode(0)
        sum_list = sum_list_head
        while l1 or l2:

            x = 0 if l1==None else l1.val
            y = 0 if l2==None else l2.val

            sum_val = carry+x+y

            carry = sum_val//10
            sum_val = sum_val%10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            sum_list.next = ListNode(sum_val)
            sum_list = sum_list.next

        if carry:
            sum_list.next = ListNode(carry)

        return sum_list_head.next
            
