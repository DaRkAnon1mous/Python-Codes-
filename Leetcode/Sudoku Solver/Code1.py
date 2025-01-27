## Best Optimized Code out of all
class Solution: 
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Track empty cells
        empty_cells = []

        def getBoxIndex(row, col):
            return (row // 3) * 3 + col // 3

        # Initialize the board state
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    value = board[r][c]
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[getBoxIndex(r, c)].add(value)

        # Function to get possible values for a cell
        def getPossibleValues(r, c):
            box_index = getBoxIndex(r, c)
            return {str(num) for num in range(1, 10)} - (rows[r] | cols[c] | boxes[box_index])

        # Sort empty cells by the number of possible values (MRV heuristic)
        empty_cells.sort(key=lambda cell: len(getPossibleValues(cell[0], cell[1])))

        # Backtracking with forward checking
        def solve(index=0):
            if index == len(empty_cells):
                return True  # Solved
            
            r, c = empty_cells[index]
            box_index = getBoxIndex(r, c)

            for num in getPossibleValues(r, c):
                # Place the number
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

                # Recurse to the next cell
                if solve(index + 1):
                    return True

                # Backtrack
                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_index].remove(num)

            return False

        solve()
