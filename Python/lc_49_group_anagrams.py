# 49. Group Anagrams
# Time: N*Mlog(M): where N is the length of strs, and M is the avg length of word in strs
# Space: O(N*M) : *M for storing the words in map.Can be reduced to constant space by using alphabet arr [0]*26.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ana_map = defaultdict(list)

        for st in strs:
            ana_map["".join(sorted(st))].append(st)


        return list(ana_map.values())
