# Review Mar 9th '20
# Time: O(len(s))
# Space: O(size(char_set))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        import collections
        ch_map = collections.defaultdict(int)

        ans = 0
        start = 0

        for index, ch in enumerate(s):

            if ch not in s:     # can combine this, and else condition, since they are same
                ch_map[ch] = index
                ans = max(ans, index-start+1)
            elif ch in ch_map and ch_map[ch]>=start:
                start = ch_map[ch]+1
                ch_map[ch] = index
            else:
                ch_map[ch] = index
                ans = max(ans, index-start+1)

        return ans

# Time: O(len(s))
# Space: O(size(char_set))

class Solution:
    """
    Cleaner solution
    """
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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        last_seen = {}
        cur_start = 0
        max_len = 0

        for index, ch in enumerate(s):

            if ch not in last_seen:
                last_seen[ch] = index
                max_len = max(max_len, index-cur_start+1)
            elif ch in last_seen and last_seen[ch]>=cur_start:
                cur_start = last_seen[ch]+1
                last_seen[ch] = index
            else:
                last_seen[ch] = index
                max_len = max(max_len, index-cur_start+1)

        return max_len
