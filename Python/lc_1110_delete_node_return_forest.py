# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        output = []
        parent = False

        self.util(root, output, to_delete, parent)

        return output

    def util(self, root, output, to_delete, parent):
        if not root:
            return None

        if root.val in to_delete:
            self.util(root.left, output, to_delete, False)
            self.util(root.right, output, to_delete, False)
            return None

        else:
            if not parent:
                output.append(root)
            root.left = self.util(root.left, output, to_delete, True)
            root.right = self.util(root.right, output, to_delete, True)

            return root
        
