# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        ans = [1]

        self.dfs(root, ans)

        return ans[0]-1


    def dfs(self, root, ans):

        if not root:
            return 0

        left = self.dfs(root.left, ans)
        right = self.dfs(root.right, ans)

        ans[0] = max(ans[0], left+right+1)

        return max(left,right)+1
