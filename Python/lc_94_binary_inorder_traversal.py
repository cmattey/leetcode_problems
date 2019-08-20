# Time: O(size(tree))
# Space: O(size(tree))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Iterative solution
        """

        if not root:
            return []

        order = []
        cur = root
        stack = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            order.append(cur.val)
            cur = cur.right

        return order


        """
    Recursive solution

        order = []
        self.inorderRec(root, order)
        return order

    def inorderRec(self, root, order):

        if not root:
            return

        self.inorderRec(root.left, order)
        order.append(root.val)
        self.inorderRec(root.right, order)
        """
        
