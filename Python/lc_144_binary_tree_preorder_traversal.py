# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
        stack = [root]
        pre = []

        while stack:
            cur_node = stack.pop()
            pre.append(cur_node.val)

            if cur_node.right:
                stack.append(cur_node.right)
            if cur_node.left:
                stack.append(cur_node.left)

        return pre
