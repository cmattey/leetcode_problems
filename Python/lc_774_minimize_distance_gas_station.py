class Solution:
    """
    TLE
    """
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        import heapq

        heap = [[-(second-first),-(second-first),0] for second,first in zip(stations[1:],stations)] # -ve to simulate max-heap

#         Structure of heap: [(max_distance, original_dist, num_stations added)]

        heapq.heapify(heap)

        for new_station in range(K):

            max_dist, orig, num_stations = heapq.heappop(heap)

            num_stations+=1
            new_min = orig/(num_stations+1)

            heapq.heappush(heap, [new_min,orig, num_stations])

        return -heapq.heappop(heap)[0]
