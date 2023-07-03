#!/usr/bin/python3

import sys


def solve_nqueens(n):
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            raise ValueError
    except ValueError:
        print("N must be an integer greater or equal to 4")
        sys.exit(1)

    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - col == i - row or col - board[i] == i - row:
                return False
        return True

    def solve(board, row):
        if row == N:
            solutions.append(board[:])
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    board[row] = col
                    solve(board, row + 1)

    solutions = []
    board = [-1] * N
    solve(board, 0)

    return solutions


if __name__ == "__main__":
    solutions = solve_nqueens(sys.argv[1])

    for sol in solutions:
        print([[i, sol[i]] for i in range(len(sol))])
