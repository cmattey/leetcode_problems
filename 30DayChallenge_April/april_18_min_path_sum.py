class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        dp_arr = [0]

        for val in grid[0]:
            dp_arr.append(dp_arr[-1]+val)
        dp_arr.pop(0)

        for row in range(1, len(grid)):
            for col in range(len(grid[0])):
                if col==0:
                    dp_arr[col] += grid[row][col]
                else:
                    dp_arr[col] = grid[row][col]+min(dp_arr[col], dp_arr[col-1])

        return dp_arr[-1]
        
