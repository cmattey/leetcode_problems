# 617. Merge Two Binary Trees
# Time: O(min(size(t1),size(t2)))
# Space: O(1) Overwriting Tree1, if creating new tree O(size(t1)+size(t2))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        node1 = t1
        node2 = t2

        if not node1:
            return node2

        if not node2:
            return node1

        if node1 and node2:
            node1.val = node1.val+node2.val

            node1.left = self.mergeTrees(node1.left,node2.left)
            node1.right = self.mergeTrees(node1.right,node2.right)


        return t1
