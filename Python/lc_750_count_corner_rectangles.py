# Time: O(m^2*n), where m,n = #row,col
# Space: O(m^2)

class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:

        row_tuples = {}

        ans = 0
        for row in range(1, len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col]!=1:
                    continue

                for r in range(row):
                    if grid[r][col]:
                        if (r,row) in row_tuples:
                            ans+=row_tuples[(r,row)]
                            row_tuples[(r,row)] +=1
                        else:
                            row_tuples[(r,row)] = 1

        return ans
        
