# Time: O(nlogn)
# Space: O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        import heapq

        if not intervals:
            return 0

        intervals.sort(key = lambda interval:interval[0])

        heap = []
        heapq.heappush(heap, intervals[0][1])

        for interval in intervals[1:]:

            if heap[0]<=interval[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, interval[1])

        return len(heap)


                    
