# 64. Minimum Path Sum
# Time: O(size(grid))
# Space: O(len(grid))
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Similar to Unique paths,
        Reduced memory from n^2 to n for this DP solution
        """
        row_cost = [float("inf")]*len(grid[0])
        row_cost[0] = 0


        for i in range(len(grid)):
            cur_col = [grid[i][0]+row_cost[0]]
            for j in range(1, len(grid[0])):
                cur_col.append(grid[i][j]+min(cur_col[-1],row_cost[j]))

            row_cost = cur_col


        return row_cost[-1]
