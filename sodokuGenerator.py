import random


class Puzzle:

    def __init__(self):
        max_attempts = 100  # stops the program after 100 attempts
        count = 1000

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
                        rand_val = random.randint(1, 9)
                        count += 1

                        if count > max_attempts: break
                    sudoku_puzzle[row][col] = rand_val

                    if count > max_attempts: break
                if count > max_attempts:
                    break

        self.completePuzzle = sudoku_puzzle

    def easy(self):
        easy_puzzle = self.completePuzzle
        to_remove = 48

        rand_row = random.randint(0, 8)
        rand_col = random.randint(0, 8)

        while to_remove > 0:
            if easy_puzzle[rand_row][rand_col] != 0:
                easy_puzzle[rand_row][rand_col] = 0
                to_remove -= 1
            rand_row = random.randint(0, 8)
            rand_col = random.randint(0, 8)

        return easy_puzzle

    def medium(self):
        medium_puzzle = self.completePuzzle
        to_remove = 54

        rand_row = random.randint(0, 8)
        rand_col = random.randint(0, 8)

        while to_remove > 0:
            if medium_puzzle[rand_row][rand_col] != 0:
                medium_puzzle[rand_row][rand_col] = 0
                to_remove -= 1
            rand_row = random.randint(0, 8)
            rand_col = random.randint(0, 8)

        return medium_puzzle

    def hard(self):
        hard_puzzle = self.completePuzzle
        to_remove = 60

        rand_row = random.randint(0, 8)
        rand_col = random.randint(0, 8)

        while to_remove > 0:
            if hard_puzzle[rand_row][rand_col] != 0:
                hard_puzzle[rand_row][rand_col] = 0
                to_remove -= 1
            rand_row = random.randint(0, 8)
            rand_col = random.randint(0, 8)

        return hard_puzzle



