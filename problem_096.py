#!/usr/bin/env python3

#https://projecteuler.net/problem=96

#file format:

#Grid 01
#003020600
#900305001
#001806400
#008102900
#700000008
#006708200
#002609500
#800203009
#005010300
#Grid 02
#200080300
#060070084
#030500209
#000105408
#000000000
#402706000
#301007040
#720040060
#004010003


from copy import deepcopy

def print_board(sudoku, debug=False):
    if not debug:
        return

    if not sudoku:
        print('broken board')
        return

    for row in sudoku:
        print(row)
    print('*#*#*')

def pad(sudoku):
    for r, row in enumerate(sudoku):
        for c, column in enumerate(row):
            if column == 0:
                sudoku[r][c] = [1,2,3,4,5,6,7,8,9]

def generate_sudoku(filename):
    with open(filename) as f:
        while True:
            sudokuname = f.readline().rstrip()
            if not sudokuname:
                break
            sudoku = []
            for line in range(9):
                sudoku.append(list(map(int, f.readline().rstrip())))
            yield sudokuname, sudoku

def row_tester(options, row, column, sudoku):
    fixed_values = [v for v in sudoku[row] if type(v) is int]
    ans = [v for v in options if v not in fixed_values]
    if len(ans) == 1:
        return ans#[0]
    return ans

def col_tester(options, row, column, sudoku):
    fixed_values = [v[column] for v in sudoku if type(v[column]) is int]
    ans = [v for v in options if v not in fixed_values]
    if len(ans) == 1:
        return ans[0]
    return ans

def square_tester(options, row, column, sudoku):
    tmp_row = row//3
    tmp_row *= 3

    tmp_col = column//3
    tmp_col *= 3

    fixed_values = [v for r in sudoku[tmp_row:tmp_row+3] for v in r[tmp_col:tmp_col+3] if type(v) is int]
    ans = [v for v in options if v not in fixed_values]

    if len(ans) == 1:
        return ans[0]
    return ans

def fixed_tester(options, row, column, sudoku):
    if type(options) is list and len(options) == 1:
        return options[0]
    else:
        return options

def eliminator(func):
    def wrapper(*args, **kwargs):
        if type(args[0]) is int:
            return args[0]
        ans = func(*args, **kwargs)
        if type(ans) is list and len(ans) == 1:
            return ans[0]
        else:
            return args[0]
    return wrapper

@eliminator
def rowliminator(options, row, column, sudoku):
    tmp_options = options
    for idx, value in enumerate(sudoku[row]):
        if idx == column:
            continue
        elif type(value) is list:
            tmp_options = [v for v in tmp_options if v not in value]
        else:
            tmp_options = [v for v in tmp_options if v != value]
    return tmp_options

@eliminator
def colliminator(options, row, column, sudoku):
    tmp_options = options
    for idxr, r in enumerate(sudoku):
        if idxr == row:
            continue
        value = r[column]
        if type(value) is list:
            tmp_options = [v for v in tmp_options if v not in value]
        else:
            tmp_options = [v for v in tmp_options if v != value]
    return tmp_options

testers = [row_tester, col_tester, square_tester, rowliminator, colliminator]

def solved(sudoku):
    for r, row in enumerate(sudoku):
       for c, column in enumerate(row):
           if type(column) is list:
               return False
           for tester in testers:
               if tester([column], r, c, sudoku) is None:
                   return False
    return True

def find_option(sudoku):
    ans = (None, None, [])
    if sudoku == None:
        return ans

    found_len = 9
    for r, row in enumerate(sudoku):
        for c, column in enumerate(row):
            if type(column) is list and len(column) <= found_len:
                ans = (r, c, column)
                found_len = len(column)
    return ans

def eliminate(sudoku, level=1):
    changed = True
    while changed:
        changed = False
        for r, row in enumerate(sudoku):
            for c, column in enumerate(row):
                if type(column) is list:
                    options = column[:]
                    for tester in testers:
                        options = tester(options, r, c, sudoku)
                        if type(options) is int:
                            break
                    if (type(options) is list and len(options) == 0) or not options:
                        return None
                    elif options != column:
                        sudoku[r][c] = options
                        changed = True
    print_board(sudoku)
    return sudoku

def solve(sudoku, level=1):

    (r, c, column) = find_option(sudoku)

    for value in column:
        ans = deepcopy(sudoku)
        print(" " * level, "guessing", r, c, value)
        ans[r][c] = value
        ans = eliminate(ans)
        ans = solve(ans, level+1)
        if ans == None:
            continue
        elif solved(ans):
            return ans
    return sudoku

total = 0
for name, sudoku in generate_sudoku('p096_sudoku.txt'):
    print(name)
    pad(sudoku)
    ans = eliminate(sudoku)
    ans = solve(ans)
    print(name, 'solution')
    print_board(ans, True)
    total += int("".join(map(str,ans[0][0:3])))
    print(total)
    print()
    #break

print(total)
