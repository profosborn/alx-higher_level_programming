#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N non-attacking queens on an NxN chessboard.
"""

import sys


class NQueens:
    """N-queens puzzle solver."""

    def __init__(self, size):
        """Initialize the NQueens object with the board size."""
        self.size = size
        self.solutions = []

    def solve(self):
        """Find all solutions to the N-queens puzzle."""
        board = [[' '] * self.size for _ in range(self.size)]
        self.place_queens(board, 0)
        self.print_solutions()

    def place_queens(self, board, row):
        """Recursively place queens on the chessboard."""
        if row == self.size:
            self.add_solution(board)
            return

        for col in range(self.size):
            if self.is_safe(board, row, col):
                board[row][col] = 'Q'
                self.place_queens(board, row + 1)
                board[row][col] = ' '

    def is_safe(self, board, row, col):
        """Check if placing a queen at the given position is safe."""
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < self.size and board[i][col + (row - i)] == 'Q':
                return False
        return True

    def add_solution(self, board):
        """Add a valid solution to the list of solutions."""
        solution = [[r, c] for r in range(self.size) for c in range(self.size) if board[r][c] == 'Q']
        self.solutions.append(solution)

    def print_solutions(self):
        """Print all solutions to the standard output."""
        for solution in self.solutions:
            print(solution)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print('N must be a number')
        sys.exit(1)
    size = int(sys.argv[1])
    if size < 4:
        print('N must be at least 4')
        sys.exit(1)

    nqueens = NQueens(size)
    nqueens.solve()
