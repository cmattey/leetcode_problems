# Time: O(k)
# Space: O(1), excluding stack else: O(k)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        self.kth = 0
        self.ans = None
        
        def inorder(root):
            if self.ans:
                return
            if not root:
                return

            inorder(root.left)
            if self.ans:
                return
            self.kth+=1
            if self.kth==k:
                self.ans = root.val
                return
            inorder(root.right)

        inorder(root)
        return self.ans
