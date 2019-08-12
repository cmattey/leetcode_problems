# 516. Longest Palindromic Subsequence
# Time: O(n^2)
# Space: O(n^2)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        dp_mat = [[0 for _ in range(len(s))]for _ in range(len(s))]

        for row in range(len(s)):
            dp_mat[row][row]=1

            if row+1 in range(len(s)):
                if s[row]==s[row+1]:
                    dp_mat[row][row+1] = 2

        # if s[i]==s[j] dp_mat[i][j] = 2+dp_mat[i+1][j-1]
        # elif s[i]!=s[j] dp_mat[i][j] = max(dp_mat[i+1][j],dp_mat[i][j-1])

        # Order of filling up the matrix is important!
        # We are essentially considering all combinations in this order:
        # [n-2..n-1], [n-3..n-1], [n-4..n-1], [0..n-1]
        for row in range(len(s)-2,-1,-1):
            for col in range(row+1, len(s)):

                if s[row]==s[col]:
                    dp_mat[row][col] = 2+dp_mat[row+1][col-1]

                else:
                    dp_mat[row][col] = max(dp_mat[row+1][col],dp_mat[row][col-1])

        return dp_mat[0][-1]
