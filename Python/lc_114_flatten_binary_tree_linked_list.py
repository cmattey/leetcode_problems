# Time: O(n), n=size(tree)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return None

        flat_left = self.flatten(root.left)
        root.left = None
        flat_right = self.flatten(root.right)

        if flat_left:
            root.right = flat_left
            temp_node = flat_left

            while temp_node.right:
                temp_node = temp_node.right

            temp_node.right = flat_right

        else:
            root.right = flat_right



        return root
