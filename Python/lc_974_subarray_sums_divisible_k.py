# Time: O(N)
# Space: O(K)

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:

        cum_sum = 0

        rem_map = {0:1}
        ans = 0

        for i in A:
            cum_sum += i

            if cum_sum%K in rem_map:
                ans+=rem_map[cum_sum%K]
                rem_map[cum_sum%K]+=1
            else:
                rem_map[cum_sum%K] = 1

        return ans

# Time: O(N)
# Space: O(N), can be reduced to O(k), by calculating cum_sum on the fly

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:

        cum_sum = [0]

        for i in A:
            cum_sum.append(cum_sum[-1]+i)

        rem_map = {0:1}
        ans = 0

        for i in range(1, len(cum_sum)):

            if cum_sum[i]%K in rem_map:
                ans+=rem_map[cum_sum[i]%K]
                rem_map[cum_sum[i]%K]+=1
            else:
                rem_map[cum_sum[i]%K] = 1

        return ans
