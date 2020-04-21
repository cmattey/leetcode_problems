# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        if not preorder:
            return None

        root = TreeNode(preorder.pop(0))

        split_index = 0
        while split_index<len(preorder) and preorder[split_index]<root.val:
            split_index +=1

        root.left = self.bstFromPreorder(preorder[:split_index])
        root.right = self.bstFromPreorder(preorder[split_index:])

        return root
