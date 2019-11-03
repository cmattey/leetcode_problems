# Time: O((logn)**2)  logn height calculation, at each node at from top to bot, which is again logn node traversals
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        total_count = 0
        left_height = self.depth(root.left)
        right_height = self.depth(root.right)

        if left_height==right_height:           # If heights are same, then we know left tree is full, and it's number of nodes are 2^height-1. we can countNodes of right subtree.
            total_count = (2**left_height - 1) + 1 + self.countNodes(root.right)  # + 1 for root

        else:
            total_count = (2**right_height -1) + 1 + self.countNodes(root.left) # +1 for root


        return total_count

    def depth(self, root):
        count = 0
        if not root:
            return 0

        while root:
            count+=1
            root = root.left

        return count



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        Normal Binary Tree approach, not utilizing complete nature of the tree

        :type root: TreeNode
        :rtype: int
        """


        if not root:
            return 0

        return 1+self.countNodes(root.left)+self.countNodes(root.right)
