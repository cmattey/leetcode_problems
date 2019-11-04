# Oct 28th '19
# Time: O(n), min(both trees)
# Space: O(h),min(heights) recursive stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        if not root1 and not root2:
            return True

        if (root1 and not root2) or (root2 and not root1):
            return False


        if root1.val==root2.val:
            return (self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right)) or self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left)
        else:
            return False

# If non-unique value: Time: 2^n
# Time: O(n), since we return as soon as mismatch
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:

        if not root1 or not root2:
            return root1==root2

        else:
            return root1.val==root2.val and \
            (self.flipEquiv(root1.left,root2.left) and \
             self.flipEquiv(root1.right,root2.right) or \
             self.flipEquiv(root1.left, root2.right) and \
             self.flipEquiv(root1.right,root2.left))
