#!/usr/bin/python3
import sys


class NQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def solve(self):
        self.place_queen([], 0)

    def place_queen(self, board, row):
        if row == self.n:
            self.solutions.append(board.copy())
        else:
            for col in range(self.n):
                if self.is_safe(board, row, col):
                    board.append([row, col])
                    self.place_queen(board, row + 1)
                    board.pop()

    def is_safe(self, board, row, col):
        for queen in board:
            r, c = queen
            if col == c or row + col == r + c or row - col == r - c:
                return False
        return True

    def print_solutions(self):
        for solution in self.solutions:
            print(solution)


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
    queens.print_solutions()
