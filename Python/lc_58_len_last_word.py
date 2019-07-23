# 58. Length of Last Word
# Time: O(len(s))
# Space: (1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if not s:
            return 0

        s = s.strip()
        print(s.split(" "))
        return len(s.split(" ")[-1])
