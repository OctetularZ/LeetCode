def isValidSudoku(board):
    current_row = 0
    current_col_next = 1
    # Checking for first condition (Each row must contain the digits 1-9 without repetition)
    while current_row != 8:
        if (board[current_row][0] == board[current_row][current_col_next]) and board[current_row][0] != "." and board[current_row][current_col_next] != ".":
            return False
        current_col_next += 1
        if current_col_next == 8:
            current_row += 1
            current_col_next = 1
    current_col = 0
    current_row = 0
    current_row_next = 1
    while current_col != 9:
        if (board[current_row][current_col] == board[current_row_next][current_col]) and board[current_row][current_col] != "." and board[current_row_next][current_col] != ".":
            return False
        current_row_next += 1
        print(current_row_next)
        if current_row_next == 9 and current_row != 8:
            current_row += 1
            current_row_next = current_row + 1
        elif current_row == 8:
            current_col += 1
            current_row = 0
            current_row_next = 1
    current_row = 0
    current_col = 0
    square_grid = []
    while current_row != 9:
        square_grid.append(board[current_row][current_col])
        square_grid.append(board[current_row][current_col + 1])
        square_grid.append(board[current_row][current_col + 2])
        current_row += 1
        if current_row % 3 == 0 and current_col != 6:
            if current_row == 3:
                current_row = 0
            elif current_row == 6:
                current_row = 3
            else:
                current_row = 6
            current_col += 3
        elif current_col == 6 and current_row % 3 == 0:
            current_col = 0
        if len(square_grid) == 9:
            square_grid = list(filter(".".__ne__, square_grid))
            if len(square_grid) != len(set(square_grid)):
                return False
            square_grid.clear()
        else:
            pass

    return True


test_board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(test_board))
