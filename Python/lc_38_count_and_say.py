# 38. Count and Say
# Time: O(2^n) # Sum of first n powers of 2, 2^(n+1)-1
# Space: O(2^n)
class Solution:
    def countAndSay(self, n: int) -> str:

        if n==1:
            return '1'

        count_arr = '1'
        for i in range(2, n+1):

            cur_row = []
            index = 0
            while index<len(count_arr):
                cur_count = 1
                cur_val = count_arr[index]
                while index+1 in range(len(count_arr)) and count_arr[index]==count_arr[index+1]:
                        cur_count+=1
                        index+=1

                cur_row.append(str(cur_count)+str(cur_val))
                index+=1

            count_arr = "".join(cur_row)

        # print(count_arr)
        return count_arr
