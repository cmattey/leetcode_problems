# 22. Generate Parentheses
# Time: O(CatalanNumber(n))
# Space: O(CatalanNumber(n))
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        sol_set = []
        cur_sol = ""

        self.util(n,cur_sol,sol_set,0,0)

        return sol_set

    def util(self,n,cur_sol,sol_set,left,right):

        if len(cur_sol)==2*n:
            sol_set.append(cur_sol)
            return

        else:
            if left<n:
                self.util(n,cur_sol+'(',sol_set,left+1,right)
            if right<left:
                self.util(n,cur_sol+')',sol_set,left,right+1)

        return
