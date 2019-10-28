# Oct 27th '19
# Time: O(n^2)
# Space: O(n)
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        min_area = float('inf')

        points.sort(key=lambda pt:pt[0])

        left_edges = {}

        for x1,y1 in points:
            for x2, y2 in points:
                if (x1==x2 and y1==y2) or y1<=y2:
                    continue

                if x1==x2:
                    if (y1,y2) not in left_edges:
                        left_edges[(y1,y2)] = x1
                    else:
                        x_dist = abs(x2-left_edges[(y1,y2)])
                        y_dist = y1-y2
                        min_area = min(min_area, x_dist*y_dist)
                        left_edges[(y1,y2)] = x1

        return min_area if min_area!=float('inf') else 0


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
