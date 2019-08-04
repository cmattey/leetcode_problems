# 236. Lowest Common Ancestor of a Binary Tree
# Time: O(size(tree))
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        """
        -> Both O(n) space and O(1) space solutions
        """

        if not root:
            return False

        if root==p or root==q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right

        """
        O(n) space solution. Using DFS path

        path1 = []
        self.dfs(root, p.val, path1)
        # print(path1)
        path2 = []
        self.dfs(root, q.val, path2)
        # print(path2)

        index1 = 0
        index2 = 0

        while index1 in range(len(path1)) and index2 in range(len(path2)):
            if path1[index1]!=path2[index2]:
                return path1[index1-1]

            else:
                index1+=1
                index2+=1

        return path1[index1-1]

    def dfs(self, root, target, path):

        if not root:
            return None

        if root.val==target:
            path.append(root)
            return 1

        path.append(root)
        if self.dfs(root.left, target, path):
            return 1
        path.pop()
        path.append(root)

        if self.dfs(root.right, target, path):
            return 1
        path.pop()
        """
