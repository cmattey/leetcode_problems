# 119. Pascal's Triangle II
# Time: O(rowIndex^2)
# Space: O(rowIndex)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        ans = [1]

        for i in range(rowIndex):
            next_level = [0]*(len(ans)+1)

            for j in range(len(next_level)):

                if j==0 or j==len(next_level)-1:
                    next_level[j]=1
                else:
                    next_level[j] = ans[j-1]+ans[j]

            ans = next_level

        return ans
