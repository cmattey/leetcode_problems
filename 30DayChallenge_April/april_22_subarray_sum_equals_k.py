class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        cum_sum = [0]

        for num in nums:
            cum_sum.append(num+cum_sum[-1])
        cum_sum.pop(0)

        seen_map = {0:1}
        ans = 0
        for csum in cum_sum:

            if csum-k in seen_map:
                ans+=seen_map[csum-k]
            seen_map[csum] = seen_map.get(csum,0)+1

        return ans


        
