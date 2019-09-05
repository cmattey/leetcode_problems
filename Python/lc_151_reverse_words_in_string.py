# Time: O(len(s))
# Space: O(len(s))

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        One-liner:
        """
        words = s.split()
        return " ".join(words[::-1])

        """
        Longer version
        """
#         words = []

#         index = 0
#         while index<len(s):
#             cur_word = []
#             while index<len(s) and  s[index]!=" ":
#                 cur_word.append(s[index])
#                 index+=1
#             while index<len(s) and s[index]==" ":
#                 index+=1

#             if cur_word:
#                 words.append("".join(cur_word))

#         words = words[::-1]

#         return " ".join(words)
        
