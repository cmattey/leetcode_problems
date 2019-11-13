# Time: 4^gold + size(grid)
# Space: size(grid)

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        max_gold = float('-inf')

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    seen = set()
                    max_gold = max(max_gold, self.dfs_util(grid, row, col, seen, 0))

        return max_gold if max_gold!=float('-inf') else 0


    def dfs_util(self, grid, row, col, seen, cur_sum):
        if (row,col) in seen or row not in range(len(grid)) or col not in range(len(grid[0])) or not grid[row][col]:
            return cur_sum

        # print(row, col)
        seen.add((row, col))

        down = self.dfs_util(grid, row+1, col, seen, cur_sum+grid[row][col])
        right = self.dfs_util(grid, row, col+1, seen, cur_sum+grid[row][col])
        up = self.dfs_util(grid, row-1, col, seen, cur_sum+grid[row][col])
        left = self.dfs_util(grid, row, col-1, seen, cur_sum+grid[row][col])

        seen.remove((row, col))
        return max(left, right, up, down)
