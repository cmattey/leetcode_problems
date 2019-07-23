# 43. Multiply Strings
# Time: O(len(num1)*(len(num2)))
# Space: O(len(num1)*(len(num2)))
class Solution:
    def multiply(self, num1: str, num2: str) -> str:


        result = [0]*(len(num1)+len(num2))
        result_pos = len(result)-1

        for i in range(len(num1)-1,-1,-1):
            temp_pos = result_pos
            carry = 0
            for j in range(len(num2)-1,-1,-1):
                prod = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))+carry+int(result[temp_pos])
                carry = prod//10
                result[temp_pos]=str(prod%10)
                temp_pos-=1

            if carry:
                result[temp_pos]=str(int(result[temp_pos])+carry)
            result_pos-=1

        i = 0
        while i <len(result)-1 and (result[i]==0 or result[i]=='0'):
            result[i]=''
            i+=1
        # print(result)
        return ''.join(result)
