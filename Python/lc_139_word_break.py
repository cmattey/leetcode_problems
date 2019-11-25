# 139. Word Break
# Nov 22nd '19
# Time: O(n^2), O(n^3), if we consider splicing?
# Space: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp approach:

        dp[i]: True if s[:i] can be broken down in to words that exist in wordDict

        dp[i] = True if s[:i] in wordDict or for some k in [0,i], s[:k],s[k:j] in wordDict

        Need to find if dp[0:len(s)] is True
        """

        dp = [True] + [False]*len(s)
        for end in range(len(s)):
            for start in range(end+1):
                if dp[end+1]:
                    continue

                if s[start:end+1] in wordDict:
                    if dp[start]:
                        dp[end+1] = True

        return dp[-1]

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
