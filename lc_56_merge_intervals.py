# 56. Merge Intervals
# Time: O(len(intervals))
# Space: O(1) except sol
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key = lambda interval: interval[0])

        sol = []

        for interval in intervals:

            if not sol or sol[-1][1]<interval[0]:
                sol.append(interval)

            elif sol[-1][1]>=interval[0]:
                sol[-1][1] = max(sol[-1][1],interval[1])

        return sol
