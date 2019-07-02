# 17. Letter Combinations of a Phone Number
# Time: O(~3^(len(digits)))
# Space: >O(~3^(len(digits))) (Since for this solution we have interim cur_sol strings as well)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        num_map = {"2":"abc",
                  "3":"def",
                  "4":"ghi",
                  "5":"jkl",
                  "6":"mno",
                  "7":"pqrs",
                  "8":"tuv",
                  "9":"wxyz",}

        result_arr = []
        cur_sol = ""
        cur_pos = 0

        self.util(cur_sol, result_arr, num_map, digits,cur_pos)

        return result_arr


    def util(self,cur_sol, result_arr, num_map, digits, cur_pos):
        if len(cur_sol)==len(digits):
            result_arr.append(cur_sol)
            return

        for ch in num_map[digits[cur_pos]]:
            self.util(cur_sol+ch,result_arr, num_map, digits, cur_pos+1)

        return
