class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        """
        Need to temp variable to make transition happen, so as not to mess up previous transitions,
        only possible if we're not utilizing all 26 characters.
        Only exception if both strings are the same.
        """
        if str1==str2:
            return True

        char_map = {}

        for index, ch in enumerate(str1):

            if char_map.setdefault(ch, str2[index])!=str2[index]:
                return False

            # if ch not in char_map:
            #     char_map[ch] = str2[index]
            # elif char_map[ch]!=str2[index]:
            #     return False

        return len(set(str2))<26

        
