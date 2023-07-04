#!/usr/bin/python3

import sys


class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def solve(self):
        self.place_queen([], 0)
        self.print_solutions()

    def place_queen(self, solution, row):
        if row == self.n:
            self.solutions.append(solution)
            return

        for col in range(self.n):
            if self.is_safe(solution, row, col):
                self.place_queen(solution + [(row, col)], row + 1)

    def is_safe(self, solution, row, col):
        for queen in solution:
            q_row, q_col = queen
            if q_col == col or q_row + q_col == row + col or q_row - q_col == row - col:
                return False
        return True

    def print_solutions(self):
        for solution in self.solutions:
            print([[r, c] for r, c in solution])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N', file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4', file=sys.stderr)
            sys.exit(1)
    except ValueError:
        print('N must be a number', file=sys.stderr)
        sys.exit(1)

    queens = NQueens(n)
    queens.solve()
