# 209. Minimum Size Subarray Sum
# Time: O(len(nums))
# Space: O(1)
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        min_range = 1<<32
        cur_sum = 0
        start = 0
        for index,num in enumerate(nums):
            cur_sum+=num

            while cur_sum>=s:
                min_range = min(min_range, index-start+1)
                # min range inside loop to get minimum range before cur_sum becomes less than s
                cur_sum-= nums[start]
                start+=1

        return min_range if min_range !=1<<32 else 0
