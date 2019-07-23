# 7. Reverse Integer
# Time: O(log(x)base10)
# Space: O(1)
class Solution:
    def reverse(self, x: int) -> int:

        isNeg = False
        if x<0:
            isNeg = True

        x = abs(x)
        rev = 0
        while x>0:
            rev = rev*10 + x%10
            x = x//10

        if not isNeg:
            if rev>math.pow(2,31)-1:
                return 0
            else:
                return rev

        if isNeg:
            rev = -1*rev
            if rev<-1*math.pow(2,31):
                return 0
            else:
                return rev
