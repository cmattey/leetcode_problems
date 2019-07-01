# 13. Roman to Integer
# Time: O(len(s))
# Space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:

        roman_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
                    'IV':4,'IX':9,
                    'XL':40,'XC':90,
                    'CD':400,'CM':900}

        num = 0
        index = 0
        while index in range(len(s)):
            if index+1 in range(len(s)):
                if s[index]+s[index+1] in roman_map:
                    num+=roman_map[s[index]+s[index+1]]
                    index+=1
                else:
                    num+=roman_map[s[index]]
            else:
                num+=roman_map[s[index]]

            index+=1

        return num
