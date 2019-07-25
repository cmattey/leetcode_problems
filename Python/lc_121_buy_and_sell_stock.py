# 121. Best Time to Buy and Sell Stock
# Time: O(len(prices))
# Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0
        min_price = prices[0]
        max_profit = float("-inf")

        for i in range(1, len(prices)):

            if prices[i]>min_price:
                cur_profit = prices[i]-min_price
                max_profit = max(max_profit, cur_profit)

            else:
                min_price = prices[i]

        return 0 if max_profit==float("-inf") else max_profit
