# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow
