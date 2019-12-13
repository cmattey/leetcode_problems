# Dec 5th '19
# Time: O(n)
# Space: O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        root = head


        next_stack = []
        prev_stack = []
        child_head_stack = []
        while root:

            while root.child is None and root.next is not None:
                root = root.next

#             child exists
            if root.child:
                child_head_stack.append(root.child)

                prev_stack.append(root)
                if root.next:
                    next_stack.append(root.next)

                root = root.child
                prev_stack[-1].child = None

#             root is None
            if root.next is None:

                if not child_head_stack:
                    return head

                child_head = child_head_stack.pop()
                prev = prev_stack.pop()
                nxt = None
                if next_stack:
                    nxt = next_stack.pop()

                prev.next = child_head
                child_head.prev = prev

                root.next = nxt
                if nxt:
                    nxt.prev = root

        return head

# Time: O(num nodes^2)
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
