# 53. Maximum Subarray

# Time: O(n)
# Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        At each num, you either start a new subarray, or continue last one.
        The decision is based on whether, add the previous number leads to a
        larger sum compared to the current element.
        cur_max = max(num, cur_max+num)
        """

        cur_max = float('-inf')
        over_all_max = float('-inf')

        for num in nums:
            cur_max = max(num, cur_max+num)
            over_all_max = max(over_all_max, cur_max)

        return over_all_max


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
