# Time: O(n)
# Space: O(k)

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        modified sliding window, using a map
        """

        if not s or not k:
            return 0

        left = 0
        index = 0
        imap = collections.defaultdict(int)
        max_dist = float('-inf')

        while index<len(s):

            imap[s[index]]+=1

            while len(imap)>k and left<len(s):
                imap[s[left]]-=1

                if imap[s[left]]<=0:
                    del imap[s[left]]
                left+=1

            max_dist = max(max_dist, index-left+1)
            index+=1

        return max_dist
