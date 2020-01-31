# Time: O(max(m,n)), m = len(l1), n = len(l2)
# Space: O(max(m,n))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    """
    Less Code repetition
    """
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


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        root = ListNode('#')
        carry = 0

        result = root
        while l1 and l2:
            cur_sum = l1.val + l2.val + carry

            carry = cur_sum//10
            cur_sum = cur_sum%10

            result.next = ListNode(cur_sum)

            l1 = l1.next
            l2 = l2.next
            result = result.next

        while l1:
            result.next = ListNode((l1.val+carry)%10)
            carry = (l1.val+carry)//10
            l1 = l1.next
            result = result.next

        while l2:
            result.next = ListNode((l2.val+carry)%10)
            carry = (l2.val+carry)//10
            l2 = l2.next
            result = result.next

        if carry:
            result.next = ListNode(1)

        return root.next
