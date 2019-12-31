# Time: O(n), worst case, n=number of nodes, if ~balanced tree O(logn)
# Space: O(n) recursion stack, else O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

        min_so_far = float('inf')
        min_node = float('inf')

        return self.util(root, target, min_so_far, min_node)


    def util(self, root, target, min_so_far, min_node):
        if not root:
            return min_node

        if root.val==target:
            min_so_far = 0
            return root.val

        if abs(root.val-target)<min_so_far:
            min_node = root.val
            min_so_far = min(abs(root.val-target),min_so_far)

        if root.val>target:
            return self.util(root.left, target, min_so_far, min_node)
        else:
            return self.util(root.right, target, min_so_far, min_node)
        
