# Time: O(size(Tree))
# Space: O(size(Tree))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        return self.util(root, float('-inf'), float('inf'))


    def util(self, root, min_val, max_val):

        if not root:
            return True
        elif root.val>=max_val or root.val<=min_val:
            return False

        return self.util(root.left, min_val, root.val) and self.util(root.right,root.val, max_val)

        
