# Time: O(n)
# Space: O(h), h=height of binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        if not root:
            return True

        val = root.val

        return self.dfs(root, val)

    def dfs(self, root, val):
        if not root:
            return True

        if root.val!=val:
            return False

        return self.dfs(root.left, val) and self.dfs(root.right, val)
