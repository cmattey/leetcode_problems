class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0

        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col]=="1" and (row, col) not in visited:
                    self.dfs(row, col, grid, visited)
                    count+=1

        return count

    def dfs(self, row, col, grid, visited):

        if row not in range(len(grid)) or col not in range(len(grid[0])) or grid[row][col]=="0":
            return

        if (row, col) in visited:
            return

        visited.add((row,col))
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]

        for dx,dy in dirs:
            self.dfs(row+dx, col+dy, grid, visited)

        return
        
