# Time: O(len(shift)+O(len(s)))
# Space: O(len(s))
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        final_mov = 0
        for dir, amount in shift:
            move = 1 if dir else -1
            final_mov += move*amount
        print(final_mov)
        mov_left = False
        if final_mov<0:
            mov_left = True

        abs_amount = abs(final_mov)%len(s)

        if abs_amount ==0:
            return s

        ans = ""
        if mov_left:
            ans = s[abs_amount:] + s[:abs_amount]
        else:
            ans = s[-abs_amount:] + s[:len(s)-abs_amount]

        return ans
