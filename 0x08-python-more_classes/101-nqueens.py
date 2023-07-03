#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def solve_nqueens(n):
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - col == i - row or board[i] - col == row - i:
                return False
        return True

    def solve(board, row, solutions):
        if row == n:
            solutions.append(board[:])
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(board, row + 1, solutions)

    board = [-1] * n
    solutions = []
    solve(board, 0, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solutions = solve_nqueens(sys.argv[1])

    for sol in solutions:
        print([[i, sol[i]] for i in range(len(sol))])
