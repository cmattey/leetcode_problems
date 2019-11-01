# Time: O(n)
# Space: O(W)

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        """
        prob[i] = prob[i-1]/W(viz. prob of i-1 * prob of getting 1 ) +prob[i-2]/W +... prob[i-W]/W
        """

        if N>=K-1+W or K==0:
            return 1

        if N<K:
            return 0

        dp_arr = [0]*(N+1)

        dp_arr[0] = 1

        prob_sum = 1 #(will represent, prob[i-1]+prob[i-2]+...prob[i-W], which is a moving window of length W)

        for i in range(1, N+1):

            dp_arr[i] = prob_sum/W

            if i<K:
                prob_sum+= dp_arr[i]
            if i>=W:
                prob_sum-= dp_arr[i-W]

        return sum(dp_arr[K:])
