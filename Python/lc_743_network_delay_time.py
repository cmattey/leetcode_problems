# Time: O(V+E)
# Space: O(times)

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:

        import heapq

        graph = collections.defaultdict(list)

        for src, tgt, wt in times:
            graph[src].append([wt, tgt])

        heap = [[0, K]] # time it took to get to start, start,

        max_time = float('-inf')
        visited = set()
#         do bfs
        while heap:
            cur_time, cur_node = heapq.heappop(heap)
            visited.add(cur_node)
            max_time = max(max_time, cur_time)
            if len(visited)==N:
                return max_time

            for time, nei in graph[cur_node]:
                if nei not in visited:
                    heapq.heappush(heap, [cur_time+time, nei])


        return max_time if len(visited)==N else -1
