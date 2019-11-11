# Time: O(size(grid))
# Space:P(size(grid))

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        count = 0
        for row in range(1,len(grid)-1):
            for col in range(1,len(grid[0])-1):
                if grid[row][col]==0:
                    if self.dfs_nobound(grid, row, col):
                        print(row, col)
                        count+=1

        return count


    def dfs_nobound(self, grid, row, col):

        if (row not in range(1,len(grid)-1) or col not in range(1, len(grid[0])-1)) and grid[row][col]==0:
            return False

        if grid[row][col]==1 or grid[row][col]=='#':
            return True

        grid[row][col]='#'

        down = self.dfs_nobound(grid, row+1, col)
        right = self.dfs_nobound(grid, row, col+1)
        up = self.dfs_nobound(grid, row-1, col)
        left = self.dfs_nobound(grid, row, col-1)

        return left and down and up and right
