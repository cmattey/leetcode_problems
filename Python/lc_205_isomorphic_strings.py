# Time: O(s)
# Space: O(t+s)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:


        imap = {}
        already_mapped = set()


        for index, ch in enumerate(s):

            if s[index] not in imap:
                if t[index] in already_mapped:
                    return False

                imap[s[index]] = t[index]
                already_mapped.add(t[index])

            if s[index] in imap:
                if t[index] != imap[s[index]]:
                    return False

        return True
                

# Time: len(s)
# Space: O(s+t)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        char_map = {}
        assigned = set()

        for si,ti in zip(s,t):
            if si not in char_map and ti not in assigned:
                char_map[si] = ti
                assigned.add(ti)
            elif si in char_map and char_map[si]==ti:
                continue
            else:
                return False

        return True
