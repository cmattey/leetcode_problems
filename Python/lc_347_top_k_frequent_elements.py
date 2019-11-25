# Time: O(nlogk)
# Space: O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        counter = collections.Counter(nums)

        heap = []

        for num, freq in counter.items():

            if len(heap)<k:
                heapq.heappush(heap, (freq,num))

            else:
                if freq>heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (freq,num))

        op = []

        while heap:
            freq,num = heapq.heappop(heap)
            op.append(num)

        return op
