# Time: O(size(tree))
# Space: O(size(tree)), for recursion stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.util(root,root)

    def util(self, root1, root2):

        if not root1 and not root2:
            return True
        elif (root1 and not root2) or (root2 and not root1) or root1.val!=root2.val:
            return False

        return self.util(root1.left,root2.right) and self.util(root1.right,root2.left)
        
