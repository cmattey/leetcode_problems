# 39. Combination Sum
# Time: O((len(candidates))^(target/avg(candidates))) Review
# Space: O(target/avg(candidates))) [depth of recursion tree?]Review
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        self.util(candidates, target, 0 , [], result)

        return result


    def util(self, candidates, target, start,  cur_res, result):

        if target<0:
            return
        if target==0:
            result.append(cur_res)
            return

        for i in range(start, len(candidates)):
            self.util(candidates, target-candidates[i], i, cur_res+[candidates[i]], result)
