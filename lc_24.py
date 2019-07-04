# 24. Swap Nodes in Pairs
# Time: O(len(list))
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head:
            return None

        cur = head

        if cur.next==None:
            return head

        dummy_head = ListNode('#')
        dummy_head.next = head
        prev = dummy_head
        second = cur.next
        while cur and second:
            prev.next = second
            cur.next = second.next
            second.next = cur

            prev = cur
            cur = cur.next
            if cur:
                second = cur.next


        return dummy_head.next
