# 100. Same Tree
# Time: O(min(size(T1),size(T2)))
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:


        if not p and not q:
            return True

        elif (p and not q) or (not p and q):
            return False

        if p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        else:
            return False
