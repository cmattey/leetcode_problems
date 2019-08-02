# 419. Battleships in a Board
# Time: O(size(board))
# Space: O(1)
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        count = 0
        for row in range(len(board)):
            for col in range(len(board[0])):

                if board[row][col]=='X' and (row==0 or board[row-1][col]=='.') and (col==0 or board[row][col-1]=='.'):
                    count+=1

        return count


        """
        Without modifying value of board, using extra memory to store visited nodes


        bs_count = 0
        visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                key = str(row)+':'+str(col)
                if (key not in visited) and board[row][col]=='X':
                    bs_count+=1
                    self.dfs(row, col, visited, board)

        # print(visited)
        return bs_count


    def dfs(self, row, col, visited, board):

        if row not in range(len(board)) or col not in range(len(board[0])):
            return

        key = str(row)+':'+str(col)
        if board[row][col]=='X' and (key not in visited):

            board[row][col]='#'
            visited.add(key)

            self.dfs(row+1, col, visited, board)
            self.dfs(row, col+1, visited, board)

        return
        """
