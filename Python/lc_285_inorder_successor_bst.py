# Time: O(height(p)), when right subtree presetn, else O(height)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init(self):
        self.found = None
        self.ans = None

    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        n = None
        if p.right: # condition when right- subtree exists
            n = p.right
            while n.left:
                n = n.left

            return n

    # condition when right-subtree doesn't exist, so successor is up the tree, so we need to do inorder traversal from root
    # and maintain a prev pointer, if prev==p, then cur = successor.
        succ = None
        while root:

            if root.val>p.val:
                succ = root
                root = root.left
            elif root.val<p.val:
                root = root.right
            elif root.val==p.val:
                break

        return succ
