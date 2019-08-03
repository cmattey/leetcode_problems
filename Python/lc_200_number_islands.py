# 200. Number of Islands
# Time: O(size(grid))
# Space: O(1) # Modifying input array
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Modifying input board, can be avoided using a visited set(row:col).
        """

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col]=='1':
                    count+=1
                    self.dfs(grid, row, col)

        return count

    def dfs(self, grid, row, col):

        if row not in range(len(grid)) or col not in range(len(grid[0])):
            return

        if grid[row][col]=='1':
            grid[row][col]='#'

            self.dfs(grid,row+1,col)
            self.dfs(grid,row,col+1)
            self.dfs(grid,row-1,col)
            self.dfs(grid,row,col-1)

        return
