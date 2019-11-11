# Time: O(m*n)
# Space: O(m*n)
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = [[0 for _ in range(m)] for _ in range(n)]

        for row, col in indices:
            for r in range(len(mat)):
                mat[r][col]+=1
            for c in range(len(mat[0])):
                mat[row][c]+=1

        ans = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]%2==1:
                    ans+=1

        return ans
