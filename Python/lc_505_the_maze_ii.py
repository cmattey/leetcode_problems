# Time: O(m*n*max(m,n)), where m=num_rows, n = num_cols
# Space: O(m*n)

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        visited = set()

        q = [(start[0],start[1], 0)]

        distance = [[float('inf') for _ in range(len(maze[0]))] for _ in range(len(maze))]
        distance[start[0]][start[1]] = 0

        while q:

            cur_row, cur_col,_ = q.pop(0)
            prev_moves = distance[cur_row][cur_col]

            # if (cur_row, cur_col) in visited:
            #     continue

            # visited.add((cur_row, cur_col))
            cur_moves = 0

#             top
            temp_row, temp_col = cur_row, cur_col
            temp_moves = 0
            while temp_row-1>=0 and maze[temp_row-1][temp_col]!=1:
                temp_moves+=1
                temp_row-=1

            if distance[cur_row][cur_col]+temp_moves < distance[temp_row][temp_col]:
                distance[temp_row][temp_col] = distance[cur_row][cur_col]+temp_moves
                q.append([temp_row,temp_col, temp_moves+prev_moves])

#             bot
            temp_row, temp_col = cur_row, cur_col
            temp_moves = 0
            while temp_row+1<len(maze) and maze[temp_row+1][temp_col]!=1:
                temp_moves+=1
                temp_row+=1

            if distance[cur_row][cur_col]+temp_moves < distance[temp_row][temp_col]:
                distance[temp_row][temp_col] = distance[cur_row][cur_col]+temp_moves
                q.append([temp_row,temp_col, temp_moves+prev_moves])

#             left
            temp_row, temp_col = cur_row, cur_col
            temp_moves = 0
            while temp_col-1>=0 and maze[temp_row][temp_col-1]!=1:
                temp_moves+=1
                temp_col-=1

            if distance[cur_row][cur_col]+temp_moves < distance[temp_row][temp_col]:
                distance[temp_row][temp_col] = distance[cur_row][cur_col]+temp_moves
                q.append([temp_row,temp_col, temp_moves+prev_moves])

#             right
            temp_moves = 0
            temp_row, temp_col = cur_row, cur_col

            while temp_col+1<len(maze[0]) and maze[temp_row][temp_col+1]!=1:
                temp_moves+=1
                temp_col+=1

            if distance[cur_row][cur_col]+temp_moves < distance[temp_row][temp_col]:
                distance[temp_row][temp_col] = distance[cur_row][cur_col]+temp_moves
                q.append([temp_row,temp_col, temp_moves+prev_moves])

        final_dist = distance[destination[0]][destination[1]]
        return final_dist if final_dist!=float('inf') else -1
