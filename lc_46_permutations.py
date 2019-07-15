# 46. Permutations
# Time: O(len(nums)!) ## n^2*len(nums)! <-- Review
# Space: O(len(nums)!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums)==1:
            return [nums]

        perms = []
        for i in range(len(nums)):
            cur = [nums[i]]

            for rest in self.permute(nums[:i]+nums[i+1:]):
                # print(cur,rest)
                perms.append(cur+rest)

        return perms
