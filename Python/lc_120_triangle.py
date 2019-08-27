# Time: O(n^2), where n is number of rows in triangle
# Space: O(n)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        dp_arr = []

        for index, row in enumerate(triangle):
            if index==0:
                dp_arr.append(row[0])
            else:
                cur_min_row = [float('inf')]*len(row)
                for index, val in enumerate(dp_arr):
                    cur_min_row[index] = min(val+row[index], cur_min_row[index])
                    cur_min_row[index+1] = min(val+row[index+1], cur_min_row[index+1])
                dp_arr = cur_min_row

        return min(dp_arr)

        
