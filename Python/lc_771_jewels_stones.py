# 771. Jewels and Stones
# Time: O(len(S))
# Space: O(len(J))
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        jewels = set(J)

        count_jewels = 0
        for stone in S:
            if stone in jewels:
                count_jewels+=1

        return count_jewels
