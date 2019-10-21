# Time: O(size(matrix))
# Space: O(1)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        max_size = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):

                if row==0 or col==0:
                    continue

                if int(matrix[row][col])==0:
                    continue

                matrix[row][col]= 1 + min(int(matrix[row-1][col-1]),int(matrix[row-1][col]),int(matrix[row][col-1]))

                max_size = max(max_size, matrix[row][col])

        one_found = 0
        if any(int(val) for row in matrix for val in row):
            one_found = 1

        return max_size**2 if max_size!=0 else one_found
