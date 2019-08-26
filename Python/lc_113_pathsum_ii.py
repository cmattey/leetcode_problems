# Time: O(n), where n=size(tree)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        cur_path = []
        paths = []

        self.util(root, sum, cur_path, paths)

        return paths

    def util(self, root, cur_sum, cur_path, paths):

        if not root:
            return

        if not root.left and not root.right:
            if cur_sum-root.val==0:
                cur_path.append(root.val)
                paths.append(cur_path[:])
                cur_path.pop()
            return

        cur_path.append(root.val)
        self.util(root.left, cur_sum-root.val,cur_path, paths)
        self.util(root.right, cur_sum-root.val,cur_path, paths)
        cur_path.pop()
        return
