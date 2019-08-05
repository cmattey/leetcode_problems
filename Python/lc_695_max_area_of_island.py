# 695. Max Area of Island
# Time: O(size(grid))
# Space: O(1) except recursion stack, since modifying grid in-place else O(size(grid))

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col]==1:

                    count = self.dfs(grid, row, col)

                    max_count = max(max_count, count)

        return max_count


    def dfs(self, grid, row, col):

        if row not in range(len(grid)) or col not in range(len(grid[0])):
            return 0

        if grid[row][col]==1:
            grid[row][col]='#'

            return 1 + self.dfs(grid, row+1, col) + self.dfs(grid, row, col+1) + self.dfs(grid, row-1, col) + self.dfs(grid, row, col-1)

        else:
            return 0
