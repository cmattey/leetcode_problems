# 83. Remove Duplicates from Sorted List
# Time: O(len(list))
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        temp = head

        while temp and temp.next:
            if temp.val==temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head
