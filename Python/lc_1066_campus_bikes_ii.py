# Oct 27th '19

# Dec 5th '19
# Time: O(PlogP), where P = permutations of picking w bikes out of b bPw = b!/(b-w)!, and we do heap operations which is logP, so PlogP
# Space: O(PlogP)
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        import heapq

        assigned_bikes = [-1]*len(bikes) # note if a worker has been assigned a bike


        total_dist = 0
        seen = set()
        heap = [( total_dist, 0, tuple(assigned_bikes))] # total_cost, worker_index, assigned_worker_arr

        while True:

            cur_dist, cur_worker, ab = heapq.heappop(heap)

            if cur_worker==len(workers):
                return cur_dist

            if (ab) in seen:
                continue

            seen.add((ab))

            for bi, bike in enumerate(bikes):
                if list(ab)[bi]==1:
                    continue

                temp_ab = list(ab[:])
                temp_ab[bi] = 1
                heapq.heappush(heap, (cur_dist+self.man_dist(workers[cur_worker], bike), cur_worker+1, tuple(temp_ab)))


    def man_dist(self, p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])





# Time: O(w*b!)
# Space: O(b) + stack space

class Solution:
    """
    Optimized by storing min values for sequence of assigned bikes
    """

    def __init__(self):
        self.min_dist = float('inf')

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        a_bikes = [-1]*len(bikes)
        bike_assign_dict = {}
        ans = self.dfs(workers, bikes, 0, 0, a_bikes, bike_assign_dict)

        print(bike_assign_dict)
        return ans


    def dfs(self, workers, bikes, cur_index, cur_dist, a_bikes, bike_assign_dict):

        if cur_index==len(workers):
            return 0

        temp = float('inf')
        if tuple(a_bikes) in bike_assign_dict:
            return bike_assign_dict[tuple(a_bikes)]

        for index, bike in enumerate(bikes):
            if a_bikes[index]!=-1:
                continue
            a_bikes[index] = 1
            temp = min(temp, self.dfs(workers, bikes, cur_index+1, cur_dist, a_bikes, bike_assign_dict) + self.man_dist(workers[cur_index],bike))
#             temp init to max, then gets values after first iteration of this loop, and
#             we take the min of all these values.
            a_bikes[index] = -1

        bike_assign_dict[tuple(a_bikes)] = temp

        # print(a_bikes)
        return temp


    def man_dist(self, p1, p2):
        return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


# Oct 27th '19
# Time: O(w*b!)
# Space: O(b) + stack space

class Solution:
    """
    Brute force recursion - TLE
    """

    def __init__(self):
        self.min_dist = float('inf')

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        a_bikes = set()
        self.dfs(workers, bikes, 0, 0, a_bikes)

        return self.min_dist


    def dfs(self, workers, bikes, cur_index, cur_dist, a_bikes):

        if cur_index==len(workers):
            self.min_dist = min(self.min_dist, cur_dist)
            return

        if cur_dist>self.min_dist:
            return

        for index, bike in enumerate(bikes):
            if index in a_bikes:
                continue
            a_bikes.add(index)
            self.dfs(workers, bikes, cur_index+1, cur_dist+self.man_dist(workers[cur_index],bike), a_bikes)
            a_bikes.remove(index)


    def man_dist(self, p1, p2):
        return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
