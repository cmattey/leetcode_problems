# Time: O(num nodes)
# Space: O(1) + recursion stack

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # print("returned:", head.val)
        if not head:
            return None

        # dummy_head = Node(None, None, head, None)
        temp = head
        while temp:

            while temp and temp.child==None:
                temp = temp.next

            if not temp:
                return head

            old_next = temp.next

            new_next = self.flatten(temp.child)

            temp.next = new_next
            new_next.prev = temp
            temp.child = None

            while new_next.next:
                new_next = new_next.next

            new_next.next = old_next
            if not old_next:
                return head
            old_next.prev = new_next
            temp = old_next
        # print("returned:", head.val)
        return head
