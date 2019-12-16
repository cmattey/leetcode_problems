# 56. Merge Intervals
# Nov 16 '19
# Time: O(nlogn), n = len(intervals)
# Space: O(1), excluding output
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        intervals.sort(key = lambda interval: interval[0])

        output = [intervals[0]]

        for interval in intervals[1:]:

            if output[-1][1] >=interval[0]:
                output[-1][1] = max(interval[1], output[-1][1])
            else:
                output.append(interval)

        return output


# Time: O(len(intervals)logn)
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


"""
Modifying Intervals in-place, without using extra space
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda k:k[0])
        index = 1

        while index<len(intervals):

            if intervals[index][0]<=intervals[index-1][1]:
                intervals[index-1][1] = max(intervals[index-1][1],intervals[index][1])
                intervals.pop(index)

            else:
                index+=1

        return intervals
"""
