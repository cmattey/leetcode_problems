# Time: O(size(maze))
# Space: O(size(maze))
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        visited = set()
        return self.dfs(maze, start[0], start[1], destination, visited)


    def dfs(self, maze, row, col, destination, visited):

        print(row, col)
        if maze[row][col]==1 or row not in range(len(maze)) or col not in range(len(maze[0])) or (row, col) in visited:
            return False

        if [row,col]==destination:
            return True

        visited.add((row, col))

#         check left extreme
        temp_col = col
        while temp_col-1>=0 and maze[row][temp_col-1]!=1:
            temp_col-=1

        if self.dfs(maze, row, temp_col, destination, visited):
            return True

#         check right extreme
        temp_col = col
        while temp_col+1<len(maze[0]) and maze[row][temp_col+1]!=1:
            temp_col+=1

        if self.dfs(maze, row, temp_col, destination, visited):
            return True

#         check top extreme
        temp_row = row
        while temp_row-1>=0 and maze[temp_row-1][col]!=1:
            temp_row-=1
        if self.dfs(maze, temp_row, col, destination, visited):
            return True

#         check bot extreme
        temp_row = row
        while temp_row+1<len(maze) and maze[temp_row+1][col]!=1:
            temp_row+=1

        if self.dfs(maze, temp_row, col, destination, visited):
            return True

        # visited.remove((row, col))
        return False
