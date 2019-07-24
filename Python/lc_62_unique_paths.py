# 62. Unique Paths
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
