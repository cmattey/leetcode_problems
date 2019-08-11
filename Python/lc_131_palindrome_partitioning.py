# 131. Palindrome Partitioning
# Time: O(2^n) where n = len(s)
# Space: O(2^n)

class Solution:
    def partition(self, s: str) -> List[List[str]]:


        sol = []
        cur_sol = []

        self.util(s, 0, sol, cur_sol)

        return sol


    def util(self, s, start_pos, sol, cur_sol):

        if "".join(cur_sol)==s:
            sol.append(cur_sol[:])
            return

        for index in range(start_pos, len(s)):

            temp_str = s[start_pos:index+1]

            if temp_str==temp_str[::-1]:

                cur_sol.append(temp_str)
                self.util(s, index+1, sol, cur_sol)
                # self.util(s, index+1, sol, cur_sol+[temp_str]) without appending and popping, this will create a new str at every recursion stack.
                cur_sol.pop()
        return
