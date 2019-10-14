# 64. Minimum Path Sum
# Time: O(m*n)
# Space: O(n), for finding path sum, O(m*n) for showing path taken

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        dp_arr = grid[0]
        parent_mat = [[None for _ in range(len(grid[0]))] for _ in range(len(grid))] # Used to store parent pointer, to show path taken

        for index in range(1, len(dp_arr)):
            dp_arr[index] +=dp_arr[index-1]
            parent_mat[0][index] = [0,index-1]

        for row in range(1,len(grid)):
            for col in range(len(grid[0])):
                if col==0:
                    dp_arr[0] = grid[row][col]+dp_arr[0]
                    parent_mat[row][0] = [row-1, 0]
                else:
                    if dp_arr[col]<dp_arr[col-1]:
                        parent_mat[row][col] = [row-1,col]
                    else:
                        parent_mat[row][col] = [row, col-1]

                    dp_arr[col] = grid[row][col]+min(dp_arr[col], dp_arr[col-1])

        path = []
        end = [len(grid)-1,len(grid[0])-1]
        path.append(end)

        parent_val = parent_mat[-1][-1]
        while True:
            next_row, next_col = parent_val[0], parent_val[1]
            path.append([next_row, next_col])
            parent_val = parent_mat[next_row][next_col]
            if not parent_val:
                break

        print(path[::-1])

        return dp_arr[-1]

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
