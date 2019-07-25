# 102. Binary Tree Level Order Traversal
# Time: O(size(Tree))
# Space: O(size(Tree))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []

        q = [root]

        level_order = []

        while q:

            cur_len = len(q)
            cur_level = []
            while cur_len>0:

                cur_node = q.pop(0)
                cur_level.append(cur_node.val)

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

                cur_len-=1

            level_order.append(cur_level)

        return level_order
