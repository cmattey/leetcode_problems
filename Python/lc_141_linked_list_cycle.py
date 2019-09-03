# Time: O(n), n = # of nodes
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False

        slow = head
        fast = head.next

        while slow and fast:

            if slow==fast:
                return True

            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break

        return False
