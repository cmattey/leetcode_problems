# Time: O(m*n*buildings)
# Space: O(m*n)

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        BFS from all buildings, at each point, store sum of distances from all nodes.
        return min_sum distance.
        """

        building_count = sum([val==1 for row in grid for val in row])

        building_seen_map = collections.defaultdict(int)
        pos_map = collections.defaultdict(int)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    if not self.bfs(grid, row, col, pos_map, building_seen_map, building_count):
                        return -1

        if len(pos_map)==0:
            return -1
        else:
            ans = [val for key, val in pos_map.items() if building_seen_map[key]==building_count]
            if len(ans)>0:
                return min(ans)
            else:
                return -1


    def bfs(self, grid, row, col, pos_map, building_seen_map, building_count):

        seen = set()
        seen.add((row, col))
        q = [(row,col,0)]

        count_ones = 1      # count number of ones touched # if multiple ones arent' connected, we can prune our search, and improve performance

        while q:

            cur_x, cur_y, dist = q.pop(0)
            dirs = [(0,-1),(0,1),(1,0),(-1,0)] # left, right, down, up

            for dx, dy in dirs:
                if cur_x+dx in range(len(grid)) and cur_y+dy in range(len(grid[0])):
                    if (cur_x+dx, cur_y+dy) not in seen:
                        seen.add((cur_x+dx,cur_y+dy))
                        if grid[cur_x+dx][cur_y+dy] == 1:
                            count_ones+=1
                        if grid[cur_x+dx][cur_y+dy] == 0:
                            building_seen_map[(cur_x+dx, cur_y+dy)]+=1
                            pos_map[(cur_x+dx, cur_y+dy)]+=dist+1
                            # print((cur_x+dx, cur_y+dy))
                            q.append((cur_x+dx, cur_y+dy, dist+1))

        return count_ones==building_count
