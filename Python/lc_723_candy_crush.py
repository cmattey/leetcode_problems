# Time: (r*c)^2
# Space: O(1), except recursive call stack

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:

        nr = len(board)
        nc = len(board[0])

        did_change = False

        for row in range(nr):
            for col in range(nc-2):

                if abs(board[row][col])==abs(board[row][col+1])==abs(board[row][col+2])!=0:
                    board[row][col]=board[row][col+1]=board[row][col+2] = -abs(board[row][col])
                    did_change = True

        for col in range(nc):
            for row in range(nr-2):

                if abs(board[row][col])==abs(board[row+1][col])==abs(board[row+2][col])!=0:
                    board[row][col]=board[row+1][col]=board[row+2][col] = -abs(board[row][col])
                    did_change = True

        for col in range(nc):
            last_nz_row = nr-1
            for row in range(nr-1, -1,-1):
                if board[row][col]>0:
                    board[last_nz_row][col] = board[row][col]
                    last_nz_row-=1


            while last_nz_row>=0:
                board[last_nz_row][col] = 0
                last_nz_row-=1

        if did_change:
            return self.candyCrush(board)

        return board
