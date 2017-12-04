import time

from mb_puzzle import Puzzle


def main():
    start = int(round(time.time() * 1000))
    sudoku = Puzzle()
    end = int(round(time.time() * 1000))
    printPuzzle(sudoku, 'Initialized Sudoku Board. Time: {}ms'.format(end - start))
    start = int(round(time.time() * 1000))
    sudoku.set_value(1, 5, 6)
    sudoku.set_value(1, 6, 6)
    end = int(round(time.time() * 1000))
    printPuzzle(sudoku, 'Set value of [1,5] to 6. Time: {}ms'.format(end - start))
    start = int(round(time.time() * 1000))
    sudoku.generate()
    end = int(round(time.time() * 1000))
    printPuzzle(sudoku, 'Generated Puzzle. Time: {}ms'.format(end - start))
    start = int(round(time.time() * 1000))
    verified = sudoku.verify()
    end = int(round(time.time() * 1000))
    print("Result of Verify: {}. Time: {}ms".format(verified, end - start))


def printPuzzle(puzzle, title):
    print(title)
    for row in puzzle.board:
        print(row)
    print()


main()
