# 54. Spiral Matrix
# Time: O(size(matrix))
# Space: O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []

        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1

        spiral = []

        direction = 'r'

        while left<right and top<bottom:


            for col in range(left,right+1):
                spiral.append(matrix[top][col])

            top+=1

            for row in range(top, bottom+1):
                spiral.append(matrix[row][right])

            right-=1

            for col in range(right, left-1,-1):
                spiral.append(matrix[bottom][col])

            bottom-=1

            for row in range(bottom, top-1, -1):
                spiral.append(matrix[row][left])

            left+=1

        if left==right:
            for row in range(top, bottom+1):
                spiral.append(matrix[row][right])

        elif top==bottom:
            for col in range(left,right+1):
                spiral.append(matrix[top][col])



        return spiral
