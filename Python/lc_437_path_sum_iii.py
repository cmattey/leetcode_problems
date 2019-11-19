# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        """
        Use cumulative sum, in each root to leaf path
        """
        run_map = collections.defaultdict(int)
        run_map[0] = 1

        run_sum = 0

        return self.dfs(root, run_map, sum, run_sum)

    def dfs(self, root, run_map, sum, run_sum):
        if not root:
            return 0

        run_sum+=root.val

        count = 0

        if run_sum-sum in run_map and run_map[run_sum-sum]>0:
            count+=run_map[run_sum-sum]

        run_map[run_sum]+=1

        left_count = self.dfs(root.left, run_map, sum, run_sum)
        right_count = self.dfs(root.right, run_map, sum, run_sum)

        run_map[run_sum]-=1

        return count+left_count+right_count
