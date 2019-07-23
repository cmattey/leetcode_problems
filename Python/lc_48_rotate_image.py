# 48. Rotate Image
# Time: O(len*width matrix)
# Space: O(1)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """
        Algo:
        1. Swap, (row, col) for each element. aka Transpose
        2. Reverse the rows
        """

        for row in range(len(matrix)):
            for col in range(row,len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
