# Time: O(n) Single pass
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        start = head
        index = 1

        p_reverse = None
        next = head.next

        while index<=n:
            if index<m:
                p_reverse = start
                start = start.next
            elif index==m:
                prev = start
                reverse_end = start
                next = start.next
                start = start.next
            elif index>=m+1 and index<=n:
                next = start.next
                start.next = prev
                prev = start
                start = next

            index+=1

        if p_reverse:
            p_reverse.next = prev
        else:
            head = prev

        if next!=reverse_end:
            reverse_end.next = next

        return head
