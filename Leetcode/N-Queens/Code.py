class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # board is a list of lists
        # we will convert this to a list of strings when we append to results
        board = [["."] * n for _ in range(n)]

        def convertBoard(board):
            # creates a new list, different from the original board list of lists.
            return ["".join(row) for row in board]

        def isValid(row, col, board):
            # check Col
            for x in range(row):
                if board[x][col] == "Q":
                    return False
            # top left diagonal
            for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[r][c] == "Q":
                    return False
            # top right diagonal
            for r, c in zip(range(row, -1, -1), range(col, n, +1)):
                if board[r][c] == "Q":
                    return False
            return True

        def positionNextQueen(board, row):
            # base case
            if row == n:
                res.append(convertBoard(board))
                return
            for col in range(n):
                if isValid(row, col, board):
                    board[row][col] = "Q"
                    positionNextQueen(board, row + 1)
                    board[row][col] = "."

        positionNextQueen(board, 0)
        return res
