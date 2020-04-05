# Time: O(n), where n = len(prices)
# Space: O(1)

# April 5th

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


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        min_price = prices[0]

        index = 1
        while index<len(prices):

            if prices[index]>min_price:
                while index<len(prices) and prices[index]>prices[index-1]:
                    index+=1

                profit+=(prices[index-1]-min_price)

            if index<len(prices):
                min_price = prices[index]
            index+=1

        return profit
