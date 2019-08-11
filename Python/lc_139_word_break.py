# 139. Word Break
# Time: O(len(s)^3)
# Space: O(len(s))

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp_arr = [True]+[False for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(i,len(s)):

                if s[i:j+1] in wordDict and dp_arr[i]:
                    dp_arr[j+1] = True

            if dp_arr[-1]:
                return True

        return dp_arr[-1]
