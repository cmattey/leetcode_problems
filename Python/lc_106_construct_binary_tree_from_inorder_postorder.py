# Time: O(n) where n = number of elements in tree
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        if not inorder or not postorder:
            return None

        root = TreeNode(postorder.pop())

        root_inorder_index = inorder.index(root.val)

        root.right = self.buildTree(inorder[root_inorder_index+1:], postorder)
        root.left = self.buildTree(inorder[:root_inorder_index], postorder)

        return root
