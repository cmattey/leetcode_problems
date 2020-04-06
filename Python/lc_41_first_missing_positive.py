# Time: O(n)
# Space: O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        for index in range(n):

            while nums[index]<=n and nums[index]>0 and nums[nums[index]-1]!=nums[index]:
                nums[nums[index]-1], nums[index] = nums[index], nums[nums[index]-1]

        for i in range(n):

            if nums[i]!=i+1:
                return i+1

        return n+1
