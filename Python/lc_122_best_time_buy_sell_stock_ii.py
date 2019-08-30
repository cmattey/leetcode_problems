# Time: O(n), where n = len(prices)
# Space: O(1)

class Solution:
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


        
