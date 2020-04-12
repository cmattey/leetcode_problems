# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        if not root:
            return 0

        self.dfs(root)

        return self.diameter-1

    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.diameter = max(self.diameter, left+right+1)

        return 1+max(left, right)

        
