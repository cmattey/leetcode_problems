# Time: O(m*n)
# Space: O(m*n)
# import numpy as np
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp_mat = [[0 for i in range(len(text2))] for j in range(len(text1))]

        for ch1 in range(len(dp_mat)):
            for ch2 in range(len(dp_mat[0])):
                if ch2==0 and text1[ch1]==text2[ch2]:
                    dp_mat[ch1][ch2]=1
                elif text1[ch1]==text2[ch2]:
                    dp_mat[ch1][ch2] = 1+ dp_mat[ch1-1][ch2-1]
                else:
                    dp_mat[ch1][ch2] = max(dp_mat[ch1-1][ch2], dp_mat[ch1][ch2-1])
        # print(np.matrix(dp_mat))
        return dp_mat[-1][-1]
