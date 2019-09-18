# Time: O(log(n))
# Space: O(log(n))

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        col_num = []

        while n>0:

            cur_char = chr(int((n-1)%26)+ord('A'))
            col_num.append(cur_char)

            n = (n-1)//26

        return "".join(col_num[::-1])
