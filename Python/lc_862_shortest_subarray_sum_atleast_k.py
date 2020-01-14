# Time: O(N)
# Space: O(N)

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        from collections import deque

        ans = float('inf')

        # Create cumulative sum array
        cum_sum = [0]
        for num in A:
            cum_sum.append(cum_sum[-1]+num)

        # q will store index of cumulative sums, that haven't been used in our shortestSubArray in order of increasing index
        q = deque()

        for index in range(len(A)+1):

            while q and cum_sum[index] - cum_sum[q[0]]>=K:  # if sum of subarray >=K
                ans = min(ans, index-q.popleft())            # update ans, and discard in decreasing order of length i.e. from left to right in queue

            while q and cum_sum[q[-1]] >= cum_sum[index]:
                q.pop()

            q.append(index)

        return ans if ans<float('inf') else -1
