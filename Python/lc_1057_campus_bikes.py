# Time: WBlogB + WlogW <<-- Review
# Space: WB

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        """
        TODO: Add documentation
        Key thing: If first value is same, heap will heapify according to second value in the object.
        Think: merge k sorted arrays
        """
        import heapq

        assigned_workers = ['#']*len(workers)

        worker_heaps = {}

        for index_w, (w_x,w_y) in enumerate(workers):

            cur_heap = []
            for index_b, (b_x,b_y) in enumerate(bikes):
                manhat_dist = abs(w_x-b_x)+abs(w_y-b_y)
                cur_heap.append((manhat_dist,index_w,index_b))
            cur_heap.sort() # Consider popping from right is better for later, therefore can sort in reverse
            worker_heaps[index_w] = cur_heap

        used_bikes = set()
        cur_heap = [heap.pop(0) for heap in worker_heaps.values()]
        heapq.heapify(cur_heap)

        while len(used_bikes)<len(workers):

            dist, index_w, index_b  = heapq.heappop(cur_heap)

            if index_b not in used_bikes:
                assigned_workers[index_w] = index_b
                used_bikes.add(index_b)
            else:
                next_val = worker_heaps[index_w].pop(0)
                heapq.heappush(cur_heap,next_val)

        return assigned_workers
