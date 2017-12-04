import Tkinter as tk
from Tkinter import Entry
from genPuzzle import Puzzle


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
                    entry = tk.Entry(self, justify="center", fg="blue", width=5)
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


def easy_mode(self):
    easy_button.destroy()
    medium_button.destroy()
    hard_button.destroy()
    sudoku = Puzzle()
    sudoku = sudoku.easy()
    t = Board(self, 9, 9, sudoku)
    t.pack(side="top", fill="x")


def medium_mode(self):
    easy_button.destroy()
    medium_button.destroy()
    hard_button.destroy()
    sudoku = Puzzle()
    sudoku = sudoku.medium()
    t = Board(self, 9, 9, sudoku)
    t.pack(side="top", fill="x")


def hard_mode(self):
    easy_button.destroy()
    medium_button.destroy()
    hard_button.destroy()
    sudoku = Puzzle()
    sudoku = sudoku.hard()
    t = Board(self, 9, 9, sudoku)
    t.pack(side="top", fill="x")


if __name__ == "__main__":
    app = SudokuApp()
    app.minsize(width=200, height=200)
    app.mainloop()
