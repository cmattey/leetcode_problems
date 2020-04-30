# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        ans = self.helper(root)
        return ans[0]

    def helper(self, root):
        if not root:
            return [float('-inf'),float('-inf')]

        left = self.helper(root.left)
        right = self.helper(root.right)

        left[1] = max(0, left[1])
        right[1] = max(0, right[1])

        path_max = max(left[0], right[0], left[1]+right[1]+root.val)

        return [path_max, max(left[1],right[1])+root.val]
