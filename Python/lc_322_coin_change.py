# 322. Coin Change
# Time: O(len(coins)*amount)
# Space: O(amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        num_arr = [amount+1]*(amount+1)
        # arr[i] represents min number of coins it takes to make i amount.
        # Initialized to amount+1 (effectively ('inf'))
        num_arr[0] = 0

        for index in range(1, len(num_arr)):

            for coin in coins:
                if index-coin>=0:
                    num_arr[index] = min(1 + num_arr[index-coin], num_arr[index])

        return num_arr[amount] if num_arr[amount]<amount+1 else -1
