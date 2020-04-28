class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        max_size = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                if matrix[row][col]=="1":
                    if row-1 in range(len(matrix)) and col-1 in range(len(matrix[0])):
                        if matrix[row-1][col]!="0" and matrix[row][col-1]!="0" and matrix[row-1][col-1]!="0":
                            matrix[row][col] = min(int(matrix[row-1][col]), int(matrix[row-1][col-1]), int(matrix[row][col-1]))+1
                            max_size = max(max_size, matrix[row][col])


                    max_size = max(max_size, 1)

        return max_size**2

        
