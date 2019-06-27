# Time: O(len(s))
# Space: O(26) = O(1) OR O(k), where k is the length of the charset

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = 0
        max_len = 0

        for index, ch in enumerate(s):

            if ch in last_seen and last_seen[ch]>=start:
                start = last_seen[ch]+1
                last_seen[ch] = index

            else:
                last_seen[ch] = index
                max_len = max(max_len, index-start+1)

        return max_len
