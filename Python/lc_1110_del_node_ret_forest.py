# 1110. Delete Nodes And Return Forest

# Time: O(n)
# Space: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        forest = []
        to_delete = set(to_delete)
        self.preorder(root, None, forest, to_delete)
        return forest

    def preorder(self, root, prev, forest, to_delete):
        if not root:
            return

        if not prev:
            if root.val not in to_delete:
                forest.append(root)

        temp_left = root.left
        temp_right = root.right
        if root.right and root.right.val in to_delete:
            root.right = None
        if root.left and root.left.val in to_delete:
            root.left = None

        self.preorder(temp_left, root if root.val not in to_delete else None, forest, to_delete)
        self.preorder(temp_right, root if root.val not in to_delete else None, forest, to_delete)

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
