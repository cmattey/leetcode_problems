# Time: O(n)
# Space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        """
        if left-child is None, then no more children should be found.
        """
        from collections import deque

        if not root:
            return True

        bfs_q = deque([root])

        no_more_children = False
        while bfs_q:

            cur_node = bfs_q.popleft()

            if cur_node.left is None:
                no_more_children = True

            if cur_node.left:
                if no_more_children:
                    return False

                bfs_q.append(cur_node.left)

            if cur_node.right is None:
                no_more_children = True

            if cur_node.right:
                if no_more_children:
                    return False
                bfs_q.append(cur_node.right)

        return True
