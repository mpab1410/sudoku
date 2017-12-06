import time

from genPuzzle import Puzzle


def main():
    start = int(round(time.time() * 1000))
    sudoku = Puzzle()
    end = int(round(time.time() * 1000))
    printPuzzle(sudoku, 'Initialized Sudoku Board. Time: {}ms'.format(end - start))
    easyBoard = Puzzle()
    verified = False
    count = 1
    start = int(round(time.time() * 1000))
    easyBoard.set_board(sudoku.hard())
    printPuzzle(easyBoard, 'Result of sudoku.easy().')
    easyBoard.solve()
    printPuzzle(easyBoard, 'Result of easyBoard.solve().')
    end = int(round(time.time() * 1000))
    print("Result of Puzzle: {}. Time: {}ms".format(easyBoard.verify(), end - start))


def printPuzzle(puzzle, title):
    print(title)
    for row in puzzle.board:
        print(row)
    print()


main()
