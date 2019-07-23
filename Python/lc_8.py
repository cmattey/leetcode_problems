# 8. String to Integer (atoi)
# Time: O(len(str))
# Space: O(len(str))
class Solution:
    def myAtoi(self, str: str) -> int:

        str = str.strip()

        if not str:
            return 0

        isNeg = False
        if str[0]=='-':
            isNeg = True
            str = str[1:]
            if not str:
                return 0
        elif str[0]=='+':
            str = str[1:]
            if not str:
                return 0

        nums = {i for i in '0123456789'}

        res = []
        for ch in str:
            if not res and ch not in nums:
                return 0
            elif ch not in nums:
                break
            else:
                res.append(ch)

        num = int("".join(res))
        if isNeg:
            num = -1*num

        if num>math.pow(2,31)-1:
            return int(math.pow(2,31)-1)
        elif num<-1*math.pow(2,31):
            return int(-1*math.pow(2,31))

        return num
