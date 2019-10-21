# Time: O(n^2)
# Space: O(n)

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        min_area = float('inf')

        points.sort()

        # print(points)

        row_tuples = {}
        for point1 in points:
            for point2 in points:
                if point1==point2 or point1[0]>point2[0]:
                    continue

                if point1[1]==point2[1]:
                    if (point1[0],point2[0]) not in row_tuples:
                        row_tuples[(point1[0],point2[0])] = point1[1]
                    else:
                        cur_area = (point2[0]-point1[0])*(point2[1]-row_tuples[(point1[0],point2[0])])
                        min_area = min(min_area, cur_area)
                        row_tuples[(point1[0],point2[0])] = point1[1]

        return min_area if min_area!=float('inf') else 0
