import random


def generateSudoku():
    board = []
    for x in xrange(9):
        num_empty_cells = random.randint(2,9)
        board_row = [random.randint(0,9) for _ in xrange(9 - num_empty_cells)]
        for _ in xrange(num_empty_cells):
            board_row.append("")
        random.shuffle(board_row)
        board.append(board_row)
    return board

def printSudoku(board):
    for x in board:
        print x


def _isValidSudoku(board, isflipped):
    for row in board:
        row_map = []
        for element in row:
            if element in row_map: return str(element) + " in " + str(row)
            if element!= '.':
                row_map.append(element)
    if isflipped: return True
    else: return _isValidSudoku(zip(*board), True)

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    return _isValidSudoku(board, False)






board = generateSudoku()
board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
printSudoku(board)
print isValidSudoku(board)