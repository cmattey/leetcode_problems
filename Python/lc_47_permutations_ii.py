# 47. Permutations II
# Time: O(len(nums)!)<--REVIEW
# Space: O(len(nums)!)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        if len(nums)==1:
            return [nums]

        perms = []

        for i in range(len(nums)):

            cur = nums[i]
            if cur in set(nums[:i]):
                continue

            for rest in self.permuteUnique(nums[:i]+nums[i+1:]):
                perms.append([cur]+rest)

        return perms
