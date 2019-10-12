# 62. Unique Paths
# Time: O(m*n)
# Space: O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp_arr = [1]*n

        for row in range(1,m):
            for col in range(1,n):
                dp_arr[col] = dp_arr[col-1] + dp_arr[col]

        return dp_arr[-1]

# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        mat = [[0 for _ in range(n)]for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    mat[i][j] = 1


        for i in range(1,m):
            for j in range(1,n):
                mat[i][j] = mat[i-1][j]+mat[i][j-1]

        return mat[-1][-1]
