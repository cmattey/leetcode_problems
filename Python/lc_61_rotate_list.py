# 61. Rotate List
# Time: O(k%len(list))
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head or not head.next:
            return head

        temp = head
        len = 0
        while temp:
            temp = temp.next
            len+=1

        k = k%len

        for i in range(k):
            head = self.rotateByOne(head)

        return head



    def rotateByOne(self, head):

        temp = head
        prev = head
        temp = temp.next

        while temp.next:
            prev = prev.next
            temp = temp.next

        temp.next = head
        prev.next = None

        return temp
