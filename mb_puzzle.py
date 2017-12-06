'''
    Michael Bailey, Bailey Henson, Brian Bulka - CS 396 - SudokuPuzzle

    This class refers to a Sudoku board

    Variables:
        board:  2D integer array which represents Sudoku board

    Functions:
        __init__:   constructor which optionally takes in an already built board
        generate:   function which creates a Sudoku board
        verify:     function which verifies if a board follows Sudoku conventions
        set_value:  function which sets a value in the matrix
'''

from random import randint


class Puzzle:
    #   https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
    #   https://stackoverflow.com/questions/2164258/multiple-constructors-in-python
    def __init__(self, board=[[0 for x in range(9)] for y in range(9)]):
        self.board = board

    def generate(self):
        max_attempts = 100  # stops the program after 100 attempts
        count = 1000
        sudoku_puzzle = [[0 for x in range(9)] for y in range(9)]
        while count > max_attempts:
            # create lists for puzzle
            sudoku_puzzle = []
            for i in range(9):
                row = []
                for j in range(9):
                    row.append(0)
                sudoku_puzzle.append(row)

            # get random value
            for row in range(9):
                for col in range(9):
                    this_row = sudoku_puzzle[row]
                    this_col = []
                    for h in range(9):
                        this_col.append(sudoku_puzzle[h][col])

                    sub_col = int(col / 3)
                    sub_row = int(row / 3)
                    sub_mat = []
                    for subR in range(3):
                        for subC in range(3):
                            sub_mat.append(sudoku_puzzle[sub_row * 3 + subR][sub_col * 3 + subC])
                    rand_val = 0
                    count = 0
                    while rand_val in this_row or rand_val in this_col or rand_val in sub_mat:
                        rand_val = randint(1, 9)
                        count += 1

                        if count > max_attempts: break
                    sudoku_puzzle[row][col] = rand_val

                    if count > max_attempts: break
                if count > max_attempts:
                    break
        self.board = sudoku_puzzle

    #   NOTE: this function assumes that all numbers will be between 1 and 9 ALWAYS
    def verify(self):
        #   check rows for duplicates
        for row in self.board:
            if len(set(row)) != 9:
                return False

        #   check columns for duplicates
        for i in range(0, len(self.board), 1):
            row = []
            for j in range(0, len(self.board[i]), 1):
                row.append(self.board[j][i])
            if len(set(row)) != 9:
                return False

        #   check sub-matrix for duplicates
        for i in range(1, 8, 3):
            for j in range(1, 8, 3):
                sub_matrix = [self.board[i - 1][j - 1], self.board[i][j - 1], self.board[i + 1][j - 1],
                              self.board[i - 1][j], self.board[i][j], self.board[i + 1][j],
                              self.board[i - 1][j + 1], self.board[i][j + 1], self.board[i + 1][j + 1]]
                if len(set(sub_matrix)) != 9:
                    return False

        return True

    def set_value(self, i, j, num):
        self.board[i][j] = num

    pass
