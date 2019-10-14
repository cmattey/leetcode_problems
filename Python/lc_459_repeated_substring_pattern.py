# Time: O(n), search for s in 2*s
# Space: O(n)

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # return s in (2*s)[1:-1]
        return s in (s[1:]+s[:-1])
        
