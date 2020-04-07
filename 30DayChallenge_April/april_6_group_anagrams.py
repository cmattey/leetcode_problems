# Time: O(nlogn*len(strs)), n=avg_len_word
# Space: O(len(strs))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        imap = defaultdict(list)

        for st in strs:
            imap[tuple(sorted(st))].append(st)

        return imap.values()
