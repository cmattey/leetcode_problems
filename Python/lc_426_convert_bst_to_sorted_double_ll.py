# Time: O(N)
# Space: O(N), worst case, recursive call-stack size, if balanced tree, O(logn)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        prev_first stores as follows:
        0th index, the previous seen node
        1st index, the first element(smallest)
        """

        if not root:
            return None

        prev_first = [None,None]

        self.inorder(root, prev_first)

        prev_first[0].right = prev_first[1]
        prev_first[1].left = prev_first[0]

        return prev_first[1]

    def inorder(self, root, pf):

        if not root:
            return None

        self.inorder(root.left, pf)

        if pf[1]==None:
            pf[1] = root
        else:
            root.left = pf[0]
            pf[0].right = root

        pf[0] = root
        self.inorder(root.right, pf)
        
