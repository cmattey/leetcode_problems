# 54. Spiral Matrix

# Time: O(size(mat))
# Space: O(1), except output array

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Shorter Code, with less code repetition
        """
        if not matrix or not matrix[0]:
            return []

        l,r = 0, len(matrix[0])-1
        u,d = 0, len(matrix)-1

        ans = []

        while l<r and u<d:
            ans.extend([matrix[u][col] for col in range(l,r)])
            ans.extend([matrix[row][r] for row in range(u,d)])
            ans.extend([matrix[d][col] for col in range(r,l,-1)])
            ans.extend([matrix[row][l] for row in range(d,u,-1)])

            l,r= l+1,r-1
            u,d = u+1,d-1


        if l==r:
            ans.extend([matrix[row][l] for row in range(u,d+1)])
        elif u==d:
            ans.extend([matrix[u][col] for col in range(l,r+1)])

        return ans


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
