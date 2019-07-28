# 4. Search a 2D Matrix
# Time: O(log(M)+log(N)), where M = len(matrix), N = len(matrix[0])
# Space: O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Run two binary searches
        """

        if not matrix or not matrix[0]:
            return False

        low = 0
        high = len(matrix)-1

        while low<=high:
            mid = (low+high)//2

            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                low = mid+1
            else:
                high = mid-1

        target_row = high

        low = 0
        high = len(matrix[0])-1

        while low<=high:
            mid = (low+high)//2

            if matrix[target_row][mid]==target:
                return True
            elif matrix[target_row][mid]<target:
                low = mid+1
            else:
                high = mid-1

        return False
