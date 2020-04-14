class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        stones = [-val for val in stones]
        heapq.heapify(stones)

        while len(stones)>1:

            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            if stone1==stone2:
                continue
            else:
                heapq.heappush(stones, -abs(stone1-stone2))

        return 0 if len(stones)==0 else -stones[0]
        
