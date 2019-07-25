# 73. Set Matrix Zeroes
# Time: O(size(matrix))
# Space: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Algo:

        -> Check if 0th row/0th col have a 0 in them.
        -> Traverse from 1st row/1st col, if encounter 0 mark the 0th row/0th for that
        position
        -> traverse first rol/col, if you find 0, mark that rol/col with 0's
        -> if first step is true for 0throw/col mark that row col to 0.
        """

        is_row_zero = False
        for col in range(len(matrix[0])):
            if matrix[0][col]==0:
                is_row_zero = True
                break

        is_col_zero = False
        for row in range(len(matrix)):
            if matrix[row][0]==0:
                is_col_zero = True
                break

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col]==0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0


        for row in range(1, len(matrix)):
            if matrix[row][0]==0:
                matrix[row] = [0]*len(matrix[0])

        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0:
                for row in range(len(matrix)):
                    matrix[row][col] = 0

        if is_row_zero:
            matrix[0] = [0]*len(matrix[0])

        if is_col_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0
