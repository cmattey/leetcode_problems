# Time: O(n)
# Space: O(1)
class Solution:
    def checkRecord(self, s: str) -> bool:

        cur_a = 0
        cur_l = 0

        for el in s:

            if el=='A':
                cur_a+=1
                if cur_a>1:
                    return False
                cur_l = 0
            elif el=='L':
                cur_l+=1
                if cur_l>2:
                    return False
            else:
                cur_l = 0

        return True
