# Time: O(m*n), m = len(word1), n = len(word2)
# Space: O(m*n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        3 options for each char
        if chars match don't need to do anything
        subprobem(i,j) = subproblem(i-1,j-1)
        else:
        subproblem(i,j) = 1 + min of(1,2,3)
        1.Insertion: subproblem(word1[i], word2[j-1])
        2.Deletion: subproblem(word[i-1], word2[j])
        3.Replacement: subproblem(word1[i-1], word2[j-1])

        """

        dp_mat = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]

        for sublen in range(len(word1)+1):    # if second word is empty
            dp_mat[sublen][0] = sublen

        for sublen in range(len(word2)+1):  # if first word is empty
            dp_mat[0][sublen] = sublen

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):

                if word1[i-1]==word2[j-1]:
                    dp_mat[i][j] = dp_mat[i-1][j-1]
                else:
                    insertion = dp_mat[i][j-1]
                    deletion = dp_mat[i-1][j]
                    replace = dp_mat[i-1][j-1]

                    dp_mat[i][j] = 1 + min(insertion, deletion, replace)

        return dp_mat[-1][-1]
