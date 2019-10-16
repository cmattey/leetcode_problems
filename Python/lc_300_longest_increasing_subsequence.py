# Time: O(n^2)
# Space: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        In dp_arr, either you increase previous subsequence or start a new one.
        """
        if not nums:
            return 0
        cur_max = None
        overall_max = None

        dp_arr = [0]*len(nums)
        for index, num in enumerate(nums):
            if index==0:
                dp_arr[index] = 1
            else:
                start = index-1
                cur_max = 0
                while start>-1:
                    if num>nums[start]:
                        cur_max = max(cur_max,dp_arr[start]+1)
                    start-=1

                dp_arr[index] = cur_max if cur_max else 1

        # print(dp_arr)
        return max(dp_arr)
