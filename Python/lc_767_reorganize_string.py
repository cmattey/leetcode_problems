# 767. Reorganize String
# Time: O(n + nlog(k)) where n is len(S), and k is 26 (alphabet size)
# Space: O(n)

class Solution:
    def reorganizeString(self, S: str) -> str:
        from collections import defaultdict
        import heapq
        """
        Algo:
        1. Map to get ch:freq
        2. Create max_heap
        3. keep pairing top two most frequent elements
        4. Keep check that max_freq element isn't >len(str)/2
        """

        ch_map = defaultdict(int)

        for ch in S:
            ch_map[ch]+=1

        heap = []
        for key,value in ch_map.items():
            heap.append((-value,key))

        heapq.heapify(heap)

        result = []

        if -heap[0][0]>math.ceil((len(S))/2):
            return ""

        while heap:

            first = heapq.heappop(heap)
            result.append(first[1])

            if heap:
                second = heapq.heappop(heap)
                result.append(second[1])

            if first[0]+1<0:
                heapq.heappush(heap,(first[0]+1,first[1]))
            if second[0]+1<0:
                heapq.heappush(heap,(second[0]+1,second[1]))

        return "".join(result)
