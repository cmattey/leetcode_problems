# 53. Maximum Subarray
# Time: O(len(nums))
# Space: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = float('-inf')
        sub_max_sum = float('-inf') # max_sum for sub_array such that current element is included

        for val in nums:
            if val>0 and sub_max_sum>=0:
                sub_max_sum +=val
            elif val>0 and sub_max_sum<=0:
                sub_max_sum = val
            elif val<=0:
                sub_max_sum = max(val, sub_max_sum+val)

            max_sum = max(max_sum, sub_max_sum)

        return max_sum
