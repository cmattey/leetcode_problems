# 5. Longest Palindromic Substring
# Time: O(n^2)
# Space: O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:

        st_mat = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            st_mat[i][i]=True

            if i+1 in range(len(s)):
                if s[i]==s[i+1]:
                    st_mat[i][i+1]=True

        st_mat[i][j]=True if st_mat[i+1][j-1]==True and s[i]==s[j]


        # Order of filling up the matrix is important!
        # We are essentially considering all combinations in this order:
        # [n-2..n-1], [n-3..n-1], [n-4..n-1], [0..n-1]
        for start in range(len(s)-2,-1,-1):
            for end in range(start+1, len(s)):

                if st_mat[start+1][end-1] and s[start]==s[end]:
                    st_mat[start][end] = True

        max_dim = (0,0)
        for row in range(len(s)):
            for col in range(row, len(s)):

                if st_mat[row][col]:
                    if col-row>max_dim[1]-max_dim[0]:
                        max_dim = (row,col)


        return s[max_dim[0]:max_dim[1]+1]
