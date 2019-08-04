# 235. Lowest Common Ancestor of a Binary Search Tree
# Time: O(log(size(tree)))
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root:
            return root

        p_val = p.val
        q_val = q.val

        while root:
            if (p_val>root.val and q_val>root.val):
                root = root.right

            elif (p_val<root.val and q_val<root.val):
                root = root.left
            else:
                return root
