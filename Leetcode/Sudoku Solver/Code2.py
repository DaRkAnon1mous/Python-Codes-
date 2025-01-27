## Best of my code but not best Time limit
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Track the numbers in rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        def getBoxIndex(row, col):
            return (row // 3) * 3 + col // 3

        # Initialize the sets
        empty_cells = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    value = board[r][c]
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[getBoxIndex(r, c)].add(value)

        def solve(index=0):
            if index == len(empty_cells):
                return True  # Solved
            r, c = empty_cells[index]
            box_index = getBoxIndex(r, c)

            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

                    # Recurse
                    if solve(index + 1):
                        return True

                    # Backtrack
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_index].remove(num)

            return False

        solve()
