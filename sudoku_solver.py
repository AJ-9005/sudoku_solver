from pprint import pprint
def find_new_slot(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col]==-1:
                return row,col
    return None,None
def is_valid(puzzle,guess,row,col):
    if guess in puzzle[row]:
        return False
    col_vals=[puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    row_start=(row//3)*3
    col_start=(col//3)*3
    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c]==guess:
                return False
    return True
def sudoku_genius(puzzle):
    row,col=find_new_slot(puzzle)
    if row is None:
        return True
    for guess in range(1,10):
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col]=guess
            if sudoku_genius(puzzle):
                return True
        puzzle[row][col]=-1
    return False
sudoku=[
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
        ]
print(sudoku_genius(sudoku))
pprint(sudoku)
