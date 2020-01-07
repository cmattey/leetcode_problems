# Time: O(max(len(num1, num2)))
# Space: O(output)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        s = []
        carry = 0

        num1 = list(num1)
        num2 = list(num2)

        while num1 or num2:

            dig1 = ord(num1.pop()) - ord('0') if len(num1)>0 else 0
            dig2 = ord(num2.pop()) - ord('0') if len(num2)>0 else 0

            s.append(str((dig1+dig2+carry)%10))
            carry = (dig1+dig2+carry)//10

        if carry:
            s.append(str(carry))

        return ''.join(s[::-1])
