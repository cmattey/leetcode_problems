# LC Contest 170
# Time: O(n^2), n=len(s)
# Space: O(n^2)

class Solution:
    def minInsertions(self, s: str) -> int:

        memo = {}
        return self.util(s, memo)

    def util(self, s, memo):
        if s in memo:
            return memo[s]

        start = 0
        end = len(s)-1

        if len(s)==1 or len(s)==0:
            return 0
        if len(s)==2 and s[0]!=s[1]:
            return 1

        if s[start]==s[end]:
            memo[s] = self.util(s[1:-1], memo)
        else:
            memo[s] = 1+min(self.util(s[1:], memo), self.util(s[:-1], memo))

        return memo[s]


        
