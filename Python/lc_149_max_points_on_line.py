# Time: O(n^2)
# Space: O(n)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """
        For each point compare with every other point, store slope
        """

        if not points:
            return 0
        if len(points)==1:
            return 1

        max_points = 0

        for index, (x,y) in enumerate(points):
            if index==0:
                continue

            cur_slope_map = {}

            same_point = 1
            verts = 1
            for x1,y1 in points[:index]:
#                 handle same point condition

                if (x,y)==(x1,y1):
                    same_point+=1
                elif x1-x == 0:
                    verts+=1
                else:
                    cur_slope = (y1-y)/(x1-x)
                    cur_slope_map[cur_slope] = cur_slope_map.get(cur_slope,1)+1

            if cur_slope_map:
                max_others = max(cur_slope_map.values())+(same_point-1)
                max_others = max(verts + same_point-1, max_others)
                max_points = max(max_points, max_others)
            else:
                max_others = max(verts, same_point)
                max_points = max(max_points, max_others)

        return max_points
