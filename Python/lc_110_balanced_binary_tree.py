# Time: O(n), where n is size(tree)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        return self.get_height(root)!=-1


    def get_height(self, root):

        if not root:
            return 0

        left_height = self.get_height(root.left)
        if left_height==-1:
            return -1

        right_height = self.get_height(root.right)
        if right_height==-1:
            return -1
        if abs(left_height-right_height)>1:
            return -1

        return max(left_height, right_height)+1




        
