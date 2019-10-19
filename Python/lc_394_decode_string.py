# Time: O(n)
# Space: O(n)
class Solution:
    def decodeString(self, s: str) -> str:

        nums = set('1234567890')

        prev_num = 0
        index = 0

        stack = []

        while index <len(s):

            if s[index]==']':

                cur_st = []

                while stack and stack[-1]!='[':
                    cur_ch = stack.pop()
                    cur_st.append(cur_ch[::-1])

                bracket = stack.pop() # remove '['
                # print(bracket)
                num = stack.pop() # get number
                # print(num)
                cur_word = "".join(cur_st)
                cur_word = cur_word[::-1]
                # print(cur_word)
                stack.append(cur_word*num)
                index+=1
                # print(stack)
            elif s[index] in nums:

                while s[index] in nums:
                    prev_num = prev_num*10 + int(s[index])
                    index+=1

                stack.append(prev_num)
                prev_num = 0
                # print(stack)
            else:
                # print(s[index])
                stack.append(s[index])
                index+=1
                # print(stack)
        decoded = "".join(stack)
        return decoded



        
