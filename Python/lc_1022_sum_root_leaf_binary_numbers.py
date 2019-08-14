# 1022. Sum of Root To Leaf Binary Numbers
# Time: Size(tree)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:

        self.dfs(root,0)

        return self.sum

    def dfs(self, root, cur_sum):
        if not root:
            return

        if not root.left and not root.right:
            cur_sum = cur_sum*2 + root.val
            self.sum+=cur_sum
            return

        self.dfs(root.left, cur_sum*2 + root.val)
        self.dfs(root.right, cur_sum*2 + root.val)
        return
