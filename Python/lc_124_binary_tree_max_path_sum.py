# Time: O(size(tree))
# Space: O(1), excluding stack space, else O(size(tree))

# March30th '20

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:

    max_sum = float('-inf')
    def maxPathSum(self, root: TreeNode) -> int:

        self.util(root)

        return self.max_sum

    def util(self, root):

        if not root:
            return 0

        left_sum = self.util(root.left)
        right_sum = self.util(root.right)

        left_sum = 0 if left_sum<0 else left_sum
        right_sum = 0 if right_sum<0 else right_sum

        cur_max = left_sum + right_sum + root.val
        self.max_sum = max(self.max_sum, cur_max)

        return max(left_sum, right_sum) + root.val

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2:

    max_sum = float('-inf') # -1<<31

    def maxPathSum(self, root: TreeNode) -> int:

        """
        Idea: At every particular node, what is the maximum sum upto that node(provided curren_node is included).
            It can either be (right), (left),(node+right),(node+left),(node+right+left),(node). Do this recursively
        """

        self.util(root)

        return self.max_sum

    def util(self, root):

        if root==None:
            return 0

        node_val = root.val

        left_sum = self.util(root.left)
        right_sum = self.util(root.right)

        max_including_cur =  max(left_sum + node_val, right_sum + node_val, right_sum + left_sum + node_val, node_val)
        if max_including_cur>self.max_sum:
            self.max_sum = max_including_cur


        return max(left_sum+node_val, right_sum+node_val, node_val) # Note, returning only sum of cur_node with left or right subtree, not with both together
