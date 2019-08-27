# Time: O(n), where n=size(tree)
# Space: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None

        q = [root]

        while q:

            cur_len = len(q)
            prev = None

            while cur_len>0:
                cur_node = q.pop(0)

                if prev:
                    prev.next = cur_node

                prev = cur_node

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

                cur_len-=1

            prev.next = None

        return root
