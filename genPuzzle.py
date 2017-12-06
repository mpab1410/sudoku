import random


class Puzzle:
    def __init__(self):
        max_attempts = 100  # stops the program after 100 attempts
        count = 1000

        while count > max_attempts:
            # create lists for puzzle
            sudoku_puzzle = []
            for i in range(9): #fills matrix to create puzzle board, i for row and j for column
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
                    for subR in range(3): #sets up sub row
                        for subC in range(3): #sets up sub column
                            sub_mat.append(
                                sudoku_puzzle[sub_row * 3 + subR][sub_col * 3 + subC]) #keeps track of the small 3x3 board in the 9x9 that the numbers follow
                    rand_val = 0
                    count = 0
                    while rand_val in this_row or rand_val in this_col or rand_val in sub_mat: #checks for the number in the sub matrix(3x3) and the whole row and column
                        rand_val = random.randint(1, 9)
                        count += 1

                        if count > max_attempts: #keeps running as long as it hasn't taken 100 attempts, breaks to next outer loop
                            break
                    sudoku_puzzle[row][col] = rand_val

                    if count > max_attempts: #keeps running as long as it hasn't taken 100 attempts, breaks to next outer loop
                        break
                if count > max_attempts: #keeps running as long as it hasn't taken 100 attempts, breaks to next outer loop
                    break

        self.board = sudoku_puzzle

    def set_board(self, value):
        self.board = value

    #function that sets the value of a cell in a board
    def set_value(self, i, j, num):
        self.board[i][j] = num

    #function to create an easy difficulty board
    def easy(self):
        easy_puzzle = self.board
        to_remove = 48

        rand_row = random.randint(0, 8)
        rand_col = random.randint(0, 8)

        #loop keeps erasing random numbers from board until it meets the set number of 48
        while to_remove > 0: #keeps erasing numbers until the to_remove quota is met
            if easy_puzzle[rand_row][rand_col] != 0: #checks to see if the spot on the board is empty or has a value, empty spaces have value of 0
                easy_puzzle[rand_row][rand_col] = 0
                to_remove -= 1
            rand_row = random.randint(0, 8)
            rand_col = random.randint(0, 8)

        return easy_puzzle

    #function to create a medium difficulty board
    def medium(self):
        medium_puzzle = self.board
        to_remove = 54

        rand_row = random.randint(0, 8)
        rand_col = random.randint(0, 8)

        #removes 54 numbers from the board to make it harder than the easy board
        while to_remove > 0: #keeps erasing numbers until the to_remove quota is met
            if medium_puzzle[rand_row][rand_col] != 0: #checks to see if the spot on the board is empty or has a value, empty spaces have value of 0
                medium_puzzle[rand_row][rand_col] = 0
                to_remove -= 1
            rand_row = random.randint(0, 8)
            rand_col = random.randint(0, 8)

        return medium_puzzle

    #function to create a high difficulty board
    def hard(self):
        hard_puzzle = self.board
        to_remove = 60

        rand_row = random.randint(0, 8) #random row in the board
        rand_col = random.randint(0, 8) #random column in the board

        #removes 60 numbers from the board to make it harder than the medium board
        while to_remove > 0: #keeps erasing numbers until the to_remove quota is met
            if hard_puzzle[rand_row][rand_col] != 0: #checks to see if the spot on the board is empty or has a value, empty spaces have value of 0
                hard_puzzle[rand_row][rand_col] = 0
                to_remove -= 1
            rand_row = random.randint(0, 8)
            rand_col = random.randint(0, 8)

        return hard_puzzle

    #function which tells if a board is a verified sudoku puzzle
    #input: self
    #output: boolean
    def verify(self):
        #   check if numbers are between 1 and 9 (inclusive)
        for row in self.board:  # collect each row
            for num in row:  # collect each value in the row
                # if the value is not between 1-9, return false
                if num not in range(1, 10):
                    return False

        #   check rows for duplicates
        for row in self.board:
            #print row          not sure if this is needed anymore. uncomment if it is still needed.
            #print len(set(row))
            if len(set(row)) != 9:  # if the set (which only contains unique numbers) is not of length 9 (there was a duplicate number between 1-9), return false
                return False

        #   check columns for duplicates
        for i in range(0, len(self.board), 1):
            col = []
            for j in range(0, len(self.board[i]), 1):
                # append values of column into array, convert to set, and check set length
                col.append(self.board[j][i])
            if len(set(col)) != 9:
                return False

        #   check sub-matrix for duplicates
        for i in range(1, 8, 3):
            for j in range(1, 8, 3):
                sub_matrix = [self.board[i - 1][j - 1], self.board[i][j - 1], self.board[i + 1][j - 1],
                              self.board[i - 1][j],     self.board[i][j],     self.board[i + 1][j],
                              self.board[i - 1][j + 1], self.board[i][j + 1], self.board[i + 1][j + 1]]  # create submatrix as 1-dim array, convert to set, and check length
                if len(set(sub_matrix)) != 9:
                    return False

        return True  # at this point, if all tests pass, it is a valid sudoku board

    #function that checks a row for a number
    def __check_row(self, rowIndex, num):
        return num in self.board[rowIndex]

    #function that checks a column for a number
    def __check_col(self, colIndex, num):
        col = list()
        for j in range(len(self.board[colIndex])):
            col.append(self.board[j][colIndex])  # collect column numbers
        return num in col

    #function that checks a submatrix for a number
    def __check_mat(self, i, j, num):
        #find center of submatrix given by row and col values
        if i in range(0, 3):
            i = 1
        if i in range(3, 6):
            i = 4
        if i in range(6, 9):
            i = 7
        if j in range(0, 3):
            j = 1
        if j in range(3, 6):
            j = 4
        if j in range(6, 9):
            j = 7

        #collect submatrix
        subMatrix = [self.board[i - 1][j - 1], self.board[i][j - 1], self.board[i + 1][j - 1], self.board[i - 1][j],
                     self.board[i][j], self.board[i + 1][j], self.board[i - 1][j + 1], self.board[i][j + 1], self.board[i + 1][j + 1]]
        return num in subMatrix

    #function that checks if a slot is "empty"
    def __empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return i, j  # return row and col value if empty
        return False, False  # if no empty slots, then return boolean values

    # function which uses backtracking to solve an incomplete board
    # input: none
    # output: boolean
    def solve(self):
        row, col = 0, 0  # set row and col to 0
        row, col = self.__empty()  # gather row and column index of empty slot
        if isinstance(row, bool):  # if returned value is boolean (no slot was found)
            return True  # return true, which loops back in recursion

        # go from one to nine
        for n in range(1, 10):
            # if it follows sudoku rules
            if not self.__check_row(row, n) and not self.__check_col(col, n) and not self.__check_mat(row, col, n):
                # set the value of the slot to the proposed num
                self.set_value(row, col, n)
                #recursively go in, and if it is solved, return true
                if self.solve():
                    return True
                #if it doesn't work out, go back and set to 0 to try and find new value
                self.set_value(row, col, 0)
        # if all else fails, return false
        return False
