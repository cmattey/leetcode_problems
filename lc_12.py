# 12. Integer to Roman
# Time: O(len(roman(num))), 8 is longest with 4 characters.
# Space: O(len(roman(num)))
class Solution:
    def intToRoman(self, num: int) -> str:

        roman_symbols = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        num_array = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

        roman = []
        start_index = 0
        while num>0:
            while num_array[start_index]<=num:
                num-=num_array[start_index]
                roman.append(roman_symbols[start_index])

            start_index+=1

        return "".join(roman)
