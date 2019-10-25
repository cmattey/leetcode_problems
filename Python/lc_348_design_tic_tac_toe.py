# Time: O(1)
# Space: O(n)

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """

        self.row = [0]*n
        self.col = [0]*n
        self.diag = 0
        self.rev_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        return self.can_win(row,col,self.n, player)


    def can_win(self, row, col, n, player):
        numAdd = 1 if player==1 else -1

        self.row[row]+=numAdd
        self.col[col]+=numAdd

        if row==col:
            self.diag+=numAdd
        if row+col==n-1:
            self.rev_diag+=numAdd

        if n in [self.row[row], self.col[col], self.diag, self.rev_diag]:
            return 1
        if -n in [self.row[row], self.col[col], self.diag, self.rev_diag]:
            return 2

        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
