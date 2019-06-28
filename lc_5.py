# Time: O(n^2)
# Space: O(n^2)

# An element of the dpmat[i][j], reprents whether s[i:j+1], is a palindrome or not.
# The base cases are:
# dpmat[i][j] = True, if i==j
# dpmat[i][j] = True, if i+1==j and s[i]==s[j]
# the dp relation then is: dpmat[i][j] = True if dpmat[i+1][j-1]==True and s[i]==s[j]
class Solution:
    def longestPalindrome(self, s: str) -> str:

        dpmat = [[False for i in range(len(s))] for i in range(len(s))]

        for row in range(len(s)):
            for col in range(len(s)):
                if row==col:
                    dpmat[row][col] = True
                if col==row+1 and s[row]==s[col]:
                    dparr[row][col] = True


        max_coords = (0,0)
        for row in range(len(s)-1,-1,-1):
            for col in range(row+1, len(s)):

                if dparr[row+1][col-1] and s[row]==s[col]:
                    dparr[row][col] = True

                if dparr[row][col]:
                    if col-row>max_coords[1]-max_coords[0]:
                        max_coords = (row,col)

        return s[max_coords[0]:max_coords[1]+1]
