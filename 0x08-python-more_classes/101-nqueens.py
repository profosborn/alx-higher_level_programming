#!/usr/bin/python3

import sys

class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        self.solutions = []

    def solve(self):
        self.place_queen(0)
        self.print_solutions()

    def place_queen(self, col):
        if col == self.n:
            self.solutions.append(self.get_solution())
            return True

        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 'Q'
                self.place_queen(col + 1)
                self.board[row][col] = ' '

    def is_safe(self, row, col):
        for c in range(col):
            if self.board[row][c] == 'Q':
                return False

        for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[r][c] == 'Q':
                return False

        for r, c in zip(range(row, self.n), range(col, -1, -1)):
            if self.board[r][c] == 'Q':
                return False

        return True

    def get_solution(self):
        return [[r, c] for r in range(self.n) for c in range(self.n) if self.board[r][c] == 'Q']

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
