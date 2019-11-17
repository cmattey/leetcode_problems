# Time: O(n)
# Space: O(1), excluding recursion stack else O(height)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        """
        Three subtrees formed after x is chosen.
        1. Left subtree
        2. Right subtree
        3. parent_x connected to remanining tree

        y can capture any of these 3. They will ensure y's win, if >n//2+1
        """

        lr = [0,0] # count of nodes in left subtree, right subtree
        self.countNodes(root,lr, x)

        max_y = max(max(lr), n-(sum(lr)+1))

        return max_y>(n//2)


    def countNodes(self, root, lr, x):

        if not root:
            return 0

        left = self.countNodes(root.left, lr, x)
        right = self.countNodes(root.right, lr, x)

        if root.val==x:
            lr[0] = left
            lr[1] = right

        return 1+left+right
