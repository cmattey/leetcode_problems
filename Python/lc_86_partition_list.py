# 86. Partition List
# Time: O(len(list))
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        if not head:
            return None

        less_head = None
        greater_head = None

        node = head

        while node:
            if node.val<x:
                if not less_head:
                    less_head = node
                    less = less_head
                else:
                    less.next = node
                    less = less.next
            else:
                if not greater_head:
                    greater_head = node
                    greater = greater_head
                else:
                    greater.next = node
                    greater = greater.next

            node = node.next

        temp = greater_head

        while temp and temp.next:
            if temp.next.val<x:
                temp.next = None
                break
            temp = temp.next

        temp = less_head

        while temp and temp.next:
            if temp.next.val>=x:
                temp.next = None
                break
            temp = temp.next

        if temp and temp.next:
            temp.next.next = greater_head
        elif temp:
            temp.next = greater_head

        # print(less_head)
        # print(greater_head)
        return less_head if less_head else greater_head
