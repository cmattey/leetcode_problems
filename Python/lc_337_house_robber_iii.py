# Time: O(n)
# Space: O(1), O(n) recursion stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:

        cur_max, nxt_val =  self.util(root)
        return max(cur_max, nxt_val)

    def util(self, root):

        if not root:
            return [0,0]

        if not root.left and not root.right:
            return [root.val, 0]

        nxt_l, nnl_max = self.util(root.left)
        nxt_r, nnr_max = self.util(root.right)

        # print(cur_max_left, lnxt_max)
        # print(cur_max_right, rnxt_max)

        # return [root.val+nnl_max+nnr_max, nxt_l+nxt_r]
        return [root.val+nnl_max+nnr_max, max(nxt_l,nnl_max)+max(nxt_r, nnr_max)]
