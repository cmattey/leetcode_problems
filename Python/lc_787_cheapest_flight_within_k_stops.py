# Time: O(E + VlogV)
# Space: O(E + V)

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        from collections import defaultdict
        import heapq

        flight_map = defaultdict(list)

        for start,end,price in flights:
            flight_map[start].append([end,price])

        # if src not in flight_map:
        #     return -1

        heap = [(0,-1,src)] # price, stops, city

        while heap:
            cur_price, stops, cur_city = heapq.heappop(heap)
            if stops > K:
                continue

            if cur_city==dst:
                return cur_price

            for neighbor, price in flight_map[cur_city]:
                heapq.heappush(heap, (price+cur_price, stops+1, neighbor))

        return -1
