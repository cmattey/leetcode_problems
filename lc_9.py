# 9. Palindrome Number
# Time: O(log(x)base10)
# Space: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Converting x to str
        """
#         x = str(x)

#         left = 0
#         right = len(x)-1

#         while left<right:
#             if x[left]!=x[right]:
#                 return False
#             left+=1
#             right-=1

#         return True

        """
        Without converting x to str
        """

        if x<0:
            return False

        rev = 0
        temp = x
        while temp>0:
            rev = rev*10 + temp%10
            temp = temp//10

        if x==rev:
            return True
        else:
            return False
