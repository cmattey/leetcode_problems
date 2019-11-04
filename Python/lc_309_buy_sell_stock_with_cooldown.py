# Time: O(n)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Using states:
        v--------<cd/rest<----|
        s1--buy-->s2--sell-->s3(no self-loop, cause rest takes to s1)
        |         |
        self     self
        loop     loop
        for      for
        rest     rest



        s1[i] = max(s1[i-1], s3[i-1])
        s2[i] = max(s2[i-1], s1[i-1]-prices[i])
        s3[i] = s2[i-1]+price[i]

        s1[0] = 0
        s2[0] = float('-inf')
        s3[0] = float('-inf')
        """
        if not prices:
            return 0
#         s1 = [0]*len(prices)
#         s2 = [0]*len(prices)
#         s3 = [0]*len(prices)

        s1_prev = 0
        s2_prev = float('-inf')
        s3_prev = float('-inf')

        for i in range(len(prices)):
            s1 = max(s1_prev, s3_prev)
            s2 = max(s2_prev, s1_prev-prices[i])
            s3 = s2_prev+prices[i]

            s1_prev,s2_prev,s3_prev = s1,s2,s3

        # print(s1,s3)
        return max(s1,s3)
