#!/usr/bin/python3

import sys


def solve_nqueens(n):
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        for i in range(row):
            if (
                board[i] == col
                or board[i] - col == row - i
                or col - board[i] == row - i
            ):
                return False
        return True

    def solve(board, row):
        if row == N:
            solutions.append(board.copy())
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(board, row + 1)

    solutions = []
    solve([-1] * N, 0)

    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if __name__ == "__main__":
    solve_nqueens(sys.argv[1])
