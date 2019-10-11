# Time: len(s)
# Space: O(1)

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

        
