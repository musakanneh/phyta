class Solution:
    def is_valid_sudoku(self, board):
        """create a set, traverse the board
        define the row, column and board keys
        
        """
        row, col, _board = set(), set(), set()
        for i in range(9):
            for j in range(9):
                grid = board[i][j]
                if grid != ".":
                    row_key = i, grid
                    col_key = j, grid
                    board_key = i // 3, j // 3, grid
                    if row_key in row or col_key in col or board_key in _board:
                        return False
                    row.add(row_key)
                    col.add(col_key)
                    _board.add(board_key)
        return True

    def is_valid_sudoku_ii(self, board):
        row_map, col_map, board_map = {}, {}, {}
        for i in range(9):
            for j in range(9):
                sudoku_grid = board[i][j]
                if sudoku_grid != ".":
                    row_key = i, sudoku_grid
                    col_key = j, sudoku_grid
                    board_key = i // 3, j // 3, sudoku_grid
                    if (row_key in row_map or col_key in col_map 
                        or board_key in board_map):
                        return False
                    row_map = row_key
                    col_map = col_key
                    board_map = board_key
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().is_valid_sudoku_ii(board))
