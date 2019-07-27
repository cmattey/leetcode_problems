# 67. Add Binary
# Time: O(max(len(a),len(b)))
# Space: O(1) , excluding output array

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        lena = len(a)-1
        lenb = len(b)-1

        ans = []
        carry = 0

        while lena>=0 or lenb>=0 or carry:

            cur_res = 0
            if lena>=0:
                cur_res+=int(a[lena])
                lena-=1

            if lenb>=0:
                cur_res+=int(b[lenb])
                lenb-=1

            cur_res+=carry
            carry = cur_res//2
            cur_res = cur_res%2
            ans = [str(cur_res)]+ans

        return "".join(ans)
