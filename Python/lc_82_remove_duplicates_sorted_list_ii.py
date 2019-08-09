# 82. Remove Duplicates from Sorted List II
# Time: O(len(list))
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        dummy_head = ListNode('#')
        dummy_head.next = head

        prev = dummy_head
        cur = head

        while cur:

            if cur.next and cur.val==cur.next.val:
                while cur.next and cur.val==cur.next.val:
                    cur = cur.next
                cur = cur.next

            else:
                prev.next = cur
                prev = prev.next
                cur = cur.next


        prev.next = cur
        return dummy_head.next
