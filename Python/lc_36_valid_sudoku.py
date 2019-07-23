# 36. Valid Sudoku
# Time: O(len(board)^2)
# Space: O(len(board))
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            if not self.validateRow(row):
                return False

        for col in range(len(board[0])):
            if not self.validateCol(col, board):
                return False

        for row in (0,3,6):
            for col in (0,3,6):
                if not self.validateSquare(row, col, board):
                    return False

        return True


    def validateRow(self, row):

        row_set = set()
        for el in row:
            if el in row_set:
                return False
            elif el!=".":
                row_set.add(el)

        return True

    def validateCol(self, col, board):

        col_set = set()
        for row in range(len(board)):
            if board[row][col] in col_set:
                return False
            elif board[row][col]!=".":
                col_set.add(board[row][col])

        return True

    def validateSquare(self, row, col, board):
        square_set = set()

        for i in range(row//3*3, row//3*3+3):
            for j in range(col//3*3, col//3*3+3):
                if board[i][j] in square_set:
                    return False
                elif board[i][j]!=".":
                    square_set.add(board[i][j])
        # print("Valid Square")
        return True
