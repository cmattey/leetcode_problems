# 29. Divide Two Integers
# Time: O(log(dividend))
# Space: O(1)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        quot_sign = (dividend<0) ^ (divisor<0)

        bit32max = math.pow(2,31)-1
        bit32min = math.pow(-2,31)

        dividend,divisor = abs(dividend), abs(divisor)

        quot = 0
        while dividend>=divisor and dividend!=0:
            count = 0
            while divisor<<count <= dividend:
                dividend -= divisor<<count
                quot+=1<<count
                count+=1


        if quot_sign:
            quot = -quot

        return int(min(max(quot,bit32min),bit32max))
