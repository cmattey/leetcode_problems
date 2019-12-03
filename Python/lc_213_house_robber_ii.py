# Time: O(n)
# Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        """

        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]

        return max(self.util(nums[:-1]), self.util(nums[1:]))

    def util(self, nums):

        # Linear Space
        # max_arr = [0]*len(nums)
        # max_arr[0] = nums[0]

        # Constant Space
        prev_max = nums[0]
        pp_max = 0

        for i in range(1, len(nums)):

            cur_max = max(nums[i] + pp_max, prev_max)
            pp_max = prev_max
            prev_max = cur_max

            max_arr[i] = max(nums[i] + max_arr[i-2], max_arr[i-1])

        return prev_max
