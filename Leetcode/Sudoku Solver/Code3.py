## Easy to understand but exceeding time limit
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        boxes = [{} for _ in range(9)]

        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]

        def getBox(row, col):
            new_c = col // 3
            new_r = (row // 3) * 3
            return new_c + new_r

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    value = board[i][j]
                    x = getBox(i, j)
                    boxes[x][value] = True
                    rows[i][value] = True
                    cols[j][value] = True

        def isValid(box, row, col, num):
            if (num in box) or (num in row) or (num in col):
                return False
            return True

        def solveBacktrack(board, boxes, rows, cols, r, c):
            if r == 9:
                return True
            if board[r][c] == ".":
                box = getBox(r, c)
                for num in range(1, 10):
                    numVal = str(num)
                    boxId = getBox(r, c)
                    box = boxes[boxId]
                    row = rows[r]
                    col = cols[c]
                    if isValid(box, row, col, numVal):
                        board[r][c] = numVal
                        box[numVal] = True
                        row[numVal] = True
                        col[numVal] = True
                        if c == 8:
                            if solveBacktrack(board, boxes, rows, cols, r + 1, 0):
                                return True
                        else:
                            if solveBacktrack(board, boxes, rows, cols, r, c + 1):
                                return True
                        # backtrack
                        del box[numVal]
                        del row[numVal]
                        del col[numVal]
                        board[r][c] = "."
                return False
            else:
                if c == 8:
                    if solveBacktrack(board, boxes, rows, cols, r + 1, 0):
                        return True
                else:
                    if solveBacktrack(board, boxes, rows, cols, r, c + 1):
                        return True

        solveBacktrack(board, boxes, rows, cols, 0, 0)
