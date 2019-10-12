# 63. Unique Paths II
# Time: O(m*n)
# Space: O(n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        dp_arr = [0]*len(obstacleGrid[0])
        if obstacleGrid[0][0]:
            return 0

        for index,val in enumerate(obstacleGrid[0]):
            if val:
                break
            dp_arr[index] = 1

        if len(obstacleGrid)>1:
            dp_arr[0] = 0 if obstacleGrid[1][0] else 1

        for row in range(1,len(obstacleGrid)):
            dp_arr[0] = dp_arr[0]*(1-obstacleGrid[row][0])
            for col in range(1,len(obstacleGrid[0])):
                if obstacleGrid[row][col]==1:
                    dp_arr[col] = 0
                else:
                    dp_arr[col] = dp_arr[col-1]+dp_arr[col]

        return dp_arr[-1]


# Time:O(size(obstacleGrid))
# Space:O(size(obstacelGrid))

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0]==1:
            return 0

        mat = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]


        for j in range(len(mat[0])):
            if obstacleGrid[0][j]==1:
                break
            else:
                mat[0][j] = 1

        for i in range(len(mat)):
            if obstacleGrid[i][0]==1:
                break
            else:
                mat[i][0] = 1

        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):

                if obstacleGrid[i][j]==1:
                    mat[i][j]=0
                else:
                    mat[i][j] = mat[i-1][j]+mat[i][j-1]

        return mat[-1][-1]
