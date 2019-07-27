# 70. Climbing Stairs
# Time: O(n)
# Space: O(1)

class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=2:
            return n

        first = 1
        second = 2

        for i in range(3,n+1):
            ans = first+second
            first = second
            second = ans

        return ans
