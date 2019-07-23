# 1110. Delete Nodes And Return Forest
# Weekly Contest 144
# Time: O(len(TreeNode))
# Space: O(len(TreeNode)) on recursion stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        forest_roots = []

        self.postOrder(root, to_delete, forest_roots)
        if root.val not in to_delete and root.val!='#':
            forest_roots.append(root)
        return forest_roots

    def postOrder(self, root, to_delete, forest_roots):
        if root==None:
            return

        self.postOrder(root.left, to_delete, forest_roots)
        self.postOrder(root.right, to_delete, forest_roots)

        # print(root.val)
        if root.left and root.left.val=='#':
            root.left = None
        if root.right and root.right.val=='#':
            root.right = None

        if root.val in to_delete:
            if root.left:
                forest_roots.append(root.left)
            if root.right:
                forest_roots.append(root.right)

            root.val = '#'

        return
