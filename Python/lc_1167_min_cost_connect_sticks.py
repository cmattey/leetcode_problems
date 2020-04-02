# Time: O(nlogn)
# Space: O(n)

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        import heapq

        heapq.heapify(sticks)

        cost = 0
        while len(sticks)>1:

            cur_cost = heapq.heappop(sticks) + heapq.heappop(sticks)

            heapq.heappush(sticks, cur_cost)
            cost += cur_cost

        return cost
        
