# 66. Plus One
# Time: len(digits)
# Space: O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        index = len(digits)-1

        while index>=0:
            if digits[index]==9:
                digits[index] = 0
                index-=1
            else:
                break

        if index==-1:
            digits = [1]+digits
        else:
            digits[index] = (digits[index]+1)

        return digits
