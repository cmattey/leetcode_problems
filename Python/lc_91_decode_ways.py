# Time: O(n)
# Space: O(1)

class Solution:
    def numDecodings(self, s: str) -> int:

        dp_prev = 0
        dp_pp = 1

        dp_prev = 1 if s[0]!='0' else 0


        for index, ch in enumerate(s):
            if index==0:
                continue

            cur_count = 0
            if 10<=int(s[index-1]+ch)<27:
                cur_count += dp_pp
                # print(int(s[index-1]+ch))
            cur_count+=(dp_prev if ch!='0' else 0)
            dp_pp = dp_prev
            dp_prev = cur_count
        return dp_prev
