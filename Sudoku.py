import Tkinter as tk
import tkMessageBox

from genPuzzle import *


class SudokuApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        global label
        label = tk.Label(self, text="Sudoku")
        label.pack()
        global easy_button
        easy_button = tk.Button(self, text="Easy", command=lambda: easy_mode(self))
        easy_button.pack()
        global medium_button
        medium_button = tk.Button(self, text="Medium", command=lambda: medium_mode(self))
        medium_button.pack()
        global hard_button
        hard_button = tk.Button(self, text="Hard", command=lambda: hard_mode(self))
        hard_button.pack()


class Board(tk.Frame):
    def __init__(self, parent, rows, columns, table):
        # use black background so it "peeks through" to
        # form grid lines
        tk.Frame.__init__(self, parent, background="black")
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                if table[row][column] != 0:
                    label = tk.Label(self, text="%d" % (table[row][column]),
                                     borderwidth=3, width=5, height=3)

                    if (column == 2 or column == 5) and (row == 2 or row == 5):
                        label.grid(row=row, column=column, sticky="nsew", padx=(1, 3), pady=(1, 3))
                    elif column == 2 or column == 5:
                        label.grid(row=row, column=column, sticky="nsew", padx=(1, 3), pady=1)
                    elif row == 2 or row == 5:
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=(1, 3))
                    else:
                        label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(label)
                else:

                    entry = tk.Entry(self, justify="center", fg="blue", width=5, validate="key", textvariable=input)
                    entry['validatecommand'] = (entry.register(testVal), '%P', '%i', '%d')
                    entry.pack(ipady=10)

                    if (column == 2 or column == 5) and (row == 2 or row == 5):
                        entry.grid(row=row, column=column, sticky="nsew", padx=(1, 3), pady=(1, 3))
                    elif column == 2 or column == 5:
                        entry.grid(row=row, column=column, sticky="nsew", padx=(1, 3), pady=1)
                    elif row == 2 or row == 5:
                        entry.grid(row=row, column=column, sticky="nsew", padx=1, pady=(1, 3))
                    else:
                        entry.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(entry)
            self._widgets.append(current_row)

        for column in range(columns):
            self.grid_columnconfigure(column, weight=1)

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

    # insert get method
    def get(self, row, column):
        widget = self._widgets[row][column]
        if widget.winfo_class() == 'Entry':
            if not widget.get():
                return False
            else:
                return widget.get()
        else:
            return widget.cget('text')


def easy_mode(self):
    easy_button.destroy()
    medium_button.destroy()
    hard_button.destroy()
    sudoku = Puzzle()
    t = Board(self, 9, 9, sudoku.easy())
    t.pack(side="left", padx=5, pady=5)
    submit_button = tk.Button(self, text="Check Answers", command=lambda: submit_answers(t))
    submit_button.pack(side="left", padx=5, pady=5)
    global solve_button
    solve_button = tk.Button(self, text="Solve for Me", command=lambda: give_up(self, sudoku, t))
    solve_button.pack(side="left", padx=5, pady=5)


def medium_mode(self):
    easy_button.destroy()
    medium_button.destroy()
    hard_button.destroy()
    sudoku = Puzzle()
    t = Board(self, 9, 9, sudoku.medium())
    t.pack(side="left", padx=5, pady=5)
    submit_button = tk.Button(self, text="Check Answers", command=lambda: submit_answers(t))
    submit_button.pack(side="left", padx=5, pady=5)
    global solve_button
    solve_button = tk.Button(self, text="Solve for Me", command=lambda: give_up(self, sudoku, t))
    solve_button.pack(side="left", padx=5, pady=5)


def hard_mode(self):
    easy_button.destroy()
    medium_button.destroy()
    hard_button.destroy()
    sudoku = Puzzle()
    t = Board(self, 9, 9, sudoku.hard())
    t.pack(side="left", padx=5, pady=5)
    submit_button = tk.Button(self, text="Check Answers", command=lambda: submit_answers(t))
    submit_button.pack(side="left", padx=5, pady=5)
    global solve_button
    solve_button = tk.Button(self, text="Solve for Me", command=lambda: give_up(self, sudoku, t))
    solve_button.pack(side="left", padx=5, pady=5)


def submit_answers(table):
    submitted_puzzle = []
    for row in range(9):
        columns = []
        for column in range(0, 9):
            insert = table.get(row, column)
            if not insert:
                tkMessageBox.showerror("Empty", "Not all answers are filled!")
                return
            else:
                columns.append(insert)
        submitted_puzzle.append(columns)
    success = verify(submitted_puzzle)
    print success
    if success:
        tkMessageBox.showinfo("Win", "You completed the Puzzle!")
    else:
        tkMessageBox.showerror("Not yet!", "Check your answers!")


def verify(board):
    #   check rows for duplicates
    for row in board:
        print row
        print len(set(row))
        if len(set(row)) != 9:
            return False

    # check columns for duplicates
    for i in range(0, len(board), 1):
        row = []
        for j in range(0, len(board[i]), 1):
            row.append(board[j][i])
        if len(set(row)) != 9:
            return False

    # check sub-matrix for duplicates
    for i in range(1, 8, 3):
        for j in range(1, 8, 3):
            sub_matrix = [board[i - 1][j - 1], board[i][j - 1], board[i + 1][j - 1],
                          board[i - 1][j], board[i][j], board[i + 1][j],
                          board[i - 1][j + 1], board[i][j + 1], board[i + 1][j + 1]]
            if len(set(sub_matrix)) != 9:
                return False

    return True


def give_up(self, puzzle, board):
    puzzle.solve()
    board = Board(self, 9, 9, puzzle.board)
    board.pack(side="right", padx=5, pady=5)
    solve_button.destroy()



# tests for input, only numbers allowed
def testVal(inStr, i, acttyp):
    ind = int(i)
    if acttyp == '1':  # insert
        if not inStr[ind].isdigit():
            return False
    return True


if __name__ == "__main__":
    app = SudokuApp()
    app.title("Sudoku")
    app.minsize(width=200, height=200)
    app.mainloop()
