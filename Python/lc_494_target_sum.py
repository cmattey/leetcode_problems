# Time: O(S*len(nums))
# Space: O(S*len(nums))
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        if not nums:
            return 0

        cur_sum = S
        start_index = 0
        cache = {}
        return self.dfs(nums, S, start_index, cache)

    def dfs(self, nums, cur_sum, cur_index, cache):

        if (cur_sum, cur_index) in cache:
            return cache[(cur_sum, cur_index)]

        if cur_index==len(nums):
            if cur_sum==0:
                return 1
            else:
                return 0

        cache[(cur_sum, cur_index)] = self.dfs(nums, cur_sum-nums[cur_index], cur_index+1, cache) + self.dfs(nums, cur_sum+nums[cur_index], cur_index+1, cache)
        return cache[(cur_sum, cur_index)]

# Time: O(2^n)
# Space: O(n)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        TLE Solution
        """
        if not nums:
            return 0

        cur_sum = S
        start_index = 0
        return self.dfs(nums, S, start_index)

    def dfs(self, nums, cur_sum, cur_index):

        if cur_index==len(nums):
            if cur_sum==0:
                return 1
            else:
                return 0

        return self.dfs(nums, cur_sum-nums[cur_index], cur_index+1) + self.dfs(nums, cur_sum+nums[cur_index], cur_index+1)
