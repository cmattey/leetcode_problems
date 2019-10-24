# Time: O(len(s))
# Space: O(len(t))

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """


        counts = collections.Counter(t)
        left = 0
        right = -1 # important, to consider single first char substrings
        req_len = len(t)

        min_dist = float('inf')

        min_substr = ""
        while right<len(s)-1:
            if req_len!=0:
                right+=1

                if s[right] in t:
                    if counts[s[right]]>0:
                        req_len-=1
                    counts[s[right]]-=1


            while req_len==0:
                if right-left<min_dist:
                    min_dist = right-left
                    min_substr =s[left: right+1]

                if s[left] in t:
                    counts[s[left]]+=1
                if counts[s[left]]>0:
                    req_len+=1

                left+=1

        return min_substr

                
