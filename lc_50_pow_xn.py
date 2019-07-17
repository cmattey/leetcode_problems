# 50. Pow(x, n)
# Time: O(log(n))
# Space: O(log(n))
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n==0:
            return 1
        if n==1:
            return x

        if n<0:
            return 1/self.myPow(x,abs(n))


        half = self.myPow(x,abs(n)//2)
        if n%2==0:
            ans = half*half
        else:
            ans = half*half*x

        return ans
