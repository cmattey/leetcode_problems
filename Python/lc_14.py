# 14. Longest Common Prefix
# Time: O(len(strs)*len(LCP))
# Space: O(len(LCP))
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
#       Without using strs.sort()
        if not strs:
            return ""
        prefix = strs[0]

        for index in range(1,len(strs)):
            new_prefix = []
            for str_index,ch in enumerate(strs[index]):
                if str_index in range(len(prefix)) and ch==prefix[str_index]:
                    new_prefix.append(ch)
                else:
                    break

            new_prefix = "".join(new_prefix)
            prefix = new_prefix
            if prefix == "":
                break

        return prefix
