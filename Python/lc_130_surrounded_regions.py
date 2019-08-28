# Time: O(size(board))
# Space: O(1)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        for row in range(len(board)):
            for col in range(len(board[0])):
                if row==0 or row==len(board)-1 or col==0 or col==len(board[0])-1:
                    self.dfs(board, row, col)


        for row in range(len(board)):
            for col in range(len(board[0])):

                if board[row][col]=='#':
                    board[row][col]='O'
                elif board[row][col]=='O':
                    board[row][col]='X'

        return board



    def dfs(self, board, row, col):

        if row not in range(len(board)) or col not in range(len(board[0])):
            return

        if board[row][col]=='O':
            board[row][col]='#'

            self.dfs(board, row+1, col)
            self.dfs(board, row, col+1)
            self.dfs(board, row-1, col)
            self.dfs(board, row, col-1)
        
