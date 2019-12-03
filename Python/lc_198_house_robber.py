# Time: O(n)
# Space: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        prev_max = nums[0]
        pp_max = 0

        for i in range(1, len(nums)):

            cur_max = max(nums[i]+pp_max, prev_max)

            pp_max = prev_max
            prev_max = cur_max

        return prev_max
        
