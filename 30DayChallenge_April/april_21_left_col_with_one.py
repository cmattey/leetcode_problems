# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        valid_rows = []
        r, c = binaryMatrix.dimensions()

        for row in range(r):
            if binaryMatrix.get(row, c-1):
                valid_rows.append(row)

        min_col = float('inf')
        for row in valid_rows:
            cur_col = self.bin_search(row, c, binaryMatrix)
            if cur_col==0:
                return 0

            min_col = min(min_col, cur_col)

        return min_col if min_col!=float('inf') else -1


    def bin_search(self, row_num, c, bMat):
        left = 0
        right = c-1

        ans = -1
        while left<=right:

            mid = (left+right)//2

            if bMat.get(row_num, mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1

        return ans
