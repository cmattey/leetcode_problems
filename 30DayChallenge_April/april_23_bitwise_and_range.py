# Time: O(1)
# Space: O(1)
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:

        num_shifts = 0
        while m!=n:

            m = m>>1
            n = n>>1
            num_shifts+=1

        return m<<num_shifts
