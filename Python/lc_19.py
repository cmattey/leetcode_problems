# 19. Remove Nth Node From End of List
# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        slow = head
        fast = head

        for i in range(n):
            fast = fast.next

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        if slow==head:
            head = head.next

        else:
            prev.next = slow.next

        return head
