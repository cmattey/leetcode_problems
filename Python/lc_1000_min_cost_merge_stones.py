# Oct 28th '19
# Time: O(n^3)
# Space: O(n^2) for dict

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        """
        Using dp

        dp[i][j] = state, min_cost to combine stones from index i to j(inclusive)

        dp[i][j] = min(dp[i][temp]+dp[temp+1][j] for temp in range(i,j, K-1))
        so k = i+(K-1), i+2*(K-1)...., because we know adding (K-1) to a pile(or min size 1) will result in a combinable length of stones.

        """

        if K>2 and len(stones)%(K-1)!=1:    # every combine, reduces len by K-1, leaving 1 element at the end, special case for K=2, which can always combine
            return -1

        cum_sum = [0]*(len(stones)+1)


        my_dict = {}

        for i in range(len(stones)):
            cum_sum[i+1] = cum_sum[i]+stones[i]

        print(cum_sum)

        return self.dp_helper(0, len(stones)-1, K, stones, cum_sum, my_dict)

    def dp_helper(self, start, end, K, stones, cum_sum,my_dict):
        if end-start+1<K:
            return 0

        if (start,end) in my_dict: # if we've already calculated the min_cost for this range.
            return my_dict[(start,end)]

        # Sorry, about the extended parameter list, you can just nest the helper function. 
        res = min(self.dp_helper(start, temp, K, stones, cum_sum, my_dict) + self.dp_helper(temp+1, end, K, stones, cum_sum, my_dict) for temp in range(start, end, K-1))
        # Splitting start-end range into various [prefix(start-temp)][suffix(temp+1,end)], and calculating min sum for each smaller range, and storing it in map later.


        if (K>2 and (end-start+1)%(K-1)==1) or K-1==1:  # basically (end-start)%(K-1)==0
            res+= cum_sum[end+1]-cum_sum[start]

        my_dict[(start, end)] = res
        return res


class Solution:
    """
    Cleaned Brute Force approach
    """
    def mergeStones(self, stones: List[int], K: int) -> int:
        """
        For each location, we have the option of starting a pile at that location.
        """

        if len(stones)<K:
            return 0

        min_cost = float('inf')
        for start in range(len(stones)-K+1):
            min_cost = min(min_cost, self.rec(stones, start, K,0))

        return min_cost

    def rec(self, stones, start, K, cur_cost):
        # print(stones)
        if len(stones)==K:
            cur_cost+=sum(stones)
            return cur_cost

        prev = stones[:start]
        next = stones[start+K:]
        merged = sum(stones[start:start+K])

        merged_stones = prev+[merged]+next

        if len(merged_stones)<K:
            return -1

        cur_min = float('inf')
        for start in range(len(merged_stones)-K+1):
            cur_min = min(cur_min, self.rec(merged_stones, start, K,cur_cost+merged))

        return cur_min


class Solution:
    """
    Recursive solution gives TLE
    """
    def __init__(self):
        self.min_count = float('inf')

    def mergeStones(self, stones: List[int], K: int) -> int:
        """
        For each location, we have the option of starting a pile at that location.
        """

        if len(stones)==1:
            return 0

        for i in range(len(stones)-K+1):
            self.rec(stones, i, K,0)

        return self.min_count if self.min_count!=float('inf') else -1

    def rec(self, stones, start, K, cur_cost):
        # print(stones)
        if len(stones)==K:
            cur_cost+=sum(stones)
            self.min_count = min(self.min_count, cur_cost)
            return

        if len(stones)<K:
            return

#       Combine step
#       Slow because of slicing, not recommended
#       Repeated calculations
        prev = stones[:start]
        next = stones[start+K:]
        merged = sum(stones[start:start+K])

        stones = prev+[merged]+next

        for i in range(len(stones)-K+1):
            self.rec(stones, i, K,cur_cost+merged)

        return
