# 973. K Closest Points to Origin
# Time: O(len(points)*log(K))
# Space: O(log(K))

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        import heapq

        heap = []
        for point in points:

            dist = math.sqrt(point[0]**2+point[1]**2)

            if len(heap)<K:
                heapq.heappush(heap, (-dist, point))
            else:
                if dist<-heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-dist, point))


        k_points = []
        for el in heap:
            k_points.append(el[1])

        return k_points
