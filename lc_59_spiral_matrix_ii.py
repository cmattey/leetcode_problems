# 59. Spiral Matrix II
# Time: (n**2)
# Space: O(1) except output matrix
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        spiral = [[0 for _ in range(n)] for _ in range(n)]
        direction = "r"

        row,col = 0,0
        for i in range(1, n*n+1):

            if direction=='r':
                spiral[row][col]=i

                col+=1

                if col==n or spiral[row][col]:
                    row+=1
                    col-=1
                    direction = 'd'

            elif direction=='d':
                spiral[row][col]=i
                row+=1

                if row==n or spiral[row][col]:
                    row-=1
                    col-=1
                    direction = 'l'

            elif direction=='l':
                spiral[row][col]=i
                col-=1

                if col==-1 or spiral[row][col]:
                    row-=1
                    col+=1
                    direction = 'u'

            elif direction=='u':
                spiral[row][col]=i
                row-=1

                if row==-1 or spiral[row][col]:
                    row+=1
                    col+=1
                    direction = 'r'
        return spiral
