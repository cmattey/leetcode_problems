# Time: O(n)
# Space: O(n)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        if len(s)>len(t):
            return self.isOneEditDistance(t, s)

        if len(t)-len(s)>1:
            return False

        for index, ch in enumerate(s):

            if ch!=t[index]:
                if len(s)==len(t):
                    return s[index+1:]==t[index+1:]
                else:
                    return s[index:]==t[index+1:]

        return len(s)==len(t)-1
        
