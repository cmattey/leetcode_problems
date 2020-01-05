# LC Contest 170
# Time: O(n)
# Space: O(n), O(1) excluding output
class Solution:
    def freqAlphabets(self, s: str) -> str:

        i = len(s)-1

        output = []
        while i>=0:

            if s[i]=='#':
                nums = s[i-2]+s[i-1]
                i-=3
            else:
                nums = s[i]
                i-=1

            output.append(chr(int(nums)+ord('a')-1))

        return ''.join(output)[::-1]
        
