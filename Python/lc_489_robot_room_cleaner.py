# Time: O(4^m*n), m= numrows, n = numcols
# Space: O(m*n),for visited set

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        _dir = 0                # 0 = up, 1 = left, 2 = down, 3 = right
        visited = set()

        start = (0,0)

        self.dfs(start[0], start[1], visited, _dir, robot)



    def dfs(self, cr, cc, visited, _dir, robot):
        # print(cr, cc)
        robot.clean()
        visited.add((cr, cc))

        directions = [(-1,0), (0,-1),(1,0),(0,1)]

        for index, temp_dir in enumerate(directions):

            new_dir = (_dir+index)%4

            new_r = cr+directions[new_dir][0]
            new_c = cc+directions[new_dir][1]

            # move = robot.move()
            # print("new", new_r, new_c, (new_r, new_c) not in visited, move)
            if ((new_r, new_c) not in visited) and robot.move():
                self.dfs(new_r, new_c, visited, new_dir, robot)

                self.backtrack_last_loc(robot)

            robot.turnLeft()


    def backtrack_last_loc(self, robot):
        robot.turnLeft()
        robot.turnLeft()
        robot.move()
        robot.turnLeft()
        robot.turnLeft()
                
