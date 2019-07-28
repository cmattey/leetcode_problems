# 69. Sqrt(x)
# Time: O(log(x))
# Space: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:

        if x==0:
            return 0

        if x in [1,2,3]:
            return 1

        low = 1
        high = x//2

        while low<=high:
            mid = (low+high)//2

            sq = mid*mid

            if sq==x:
                return mid

            elif sq<x and (mid+1)*(mid+1)>x:
                return mid

            elif sq>x:
                high = mid-1
            else:
                low = mid+1
