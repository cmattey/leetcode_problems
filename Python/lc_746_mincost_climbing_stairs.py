# 746. Min Cost Climbing Stairs
# Time: O(len(cost))
# Space: O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        second_last_cost = cost[0]
        last_cost = cost[1]
        cur_cost = float('inf')

        index = 2
        while index < len(cost):

            cur_cost = cost[index]+min(second_last_cost,last_cost)

            second_last_cost = last_cost
            last_cost = cur_cost

            index+=1

        return min(last_cost,second_last_cost)
