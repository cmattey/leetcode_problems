# 90. Subsets II
# Time: O((2^len(nums)*)n)
# Space: O((2^len(nums))*n)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        results = [[]]

        for index, num in enumerate(nums):

            if index==0 or nums[index]!=nums[index-1]:
                l = len(results)

            for i in range(len(results)-l, len(results)):
                results.append(results[i]+[num])

        return results
