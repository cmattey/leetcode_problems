# 40. Combination Sum II
# Time:
# Space:
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()
        self.util(candidates, target, 0, [], result)

        return result

    def util(self, candidates, target, start, cur_result, result):

        if target==0:
            result.append(list(cur_result))
            return
        elif target<=0 or start>=len(candidates):
            return

        i = start
        while i < len(candidates):
            cur_result.append(candidates[i])
            self.util(candidates, target-candidates[i], i+1, cur_result, result)
            cur_result.pop()

            i+=1
            while i-1 >=0 and i<len(candidates) and candidates[i]==candidates[i-1]:
                i+=1

        return
