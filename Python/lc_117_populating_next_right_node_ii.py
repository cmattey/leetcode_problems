# Time: O(n)
# Space: O(n), Can be done in O(1)

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

            level_len = len(q)

            prev_right = None
            while level_len>0:

                cur_node = q.pop(0)                 # Pop from left

                cur_node.next = prev_right          # Assign previous right
                prev_right = cur_node

                if cur_node.right:
                    q.append(cur_node.right)        # Append right node first, so it can be popped first
                if cur_node.left:
                    q.append(cur_node.left)

                level_len-=1

        return root
