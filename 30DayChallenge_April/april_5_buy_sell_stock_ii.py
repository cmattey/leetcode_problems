# Time: O(n)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        nums = prices

        profit = 0

        start, end = 0,1

        while end<len(nums):

            if nums[start]>=nums[end]:
                start = end
                end +=1
            else:
                while end+1<len(nums) and nums[end]<nums[end+1]:
                    end+=1

                profit+=nums[end]-nums[start]

                start = end
                end +=1

        return profit
