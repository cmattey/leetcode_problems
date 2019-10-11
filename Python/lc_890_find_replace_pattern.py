# Time: #words*avg(word_size)
# Space: O(1), excluding output

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        matches = []

        for word in words:

            assigned_chars = set()
            ch_map = {}
            for index, ch in enumerate(word):

                if pattern[index] not in ch_map and ch not in assigned_chars:
                    ch_map[pattern[index]] = ch
                    assigned_chars.add(ch)
                elif pattern[index] in ch_map:
                    if not ch_map[pattern[index]]==ch:
                        break
                else:
                    break

                if index==len(word)-1:
                    matches.append(word)

        return matches
                
