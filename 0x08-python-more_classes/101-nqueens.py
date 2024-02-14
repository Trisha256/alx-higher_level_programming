#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    # Check if a queen can be placed at the given position
    # without attacking any other queen on the board

    # Check row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col):
    # Recursive function to solve the N-Queens problem

    # Base case: If all queens are placed, print the solution
    if col >= N:
        print_solution(board)
        return

    # Try placing a queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen on the board
            board[i][col] = 1

            # Recur for the next column
            solve_nqueens(board, col + 1)

            # Backtrack and remove the queen from the board
            board[i][col] = 0

def print_solution(board):
    # Print the board configuration for a valid solution
    solution = []
    for i in range(N):
        row = ""
        for j in range(N):
            if board[i][j] == 1:
                row += "Q "
            else:
                row += ". "
        solution.append(row.strip())
    print("\n".join(solution))

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command line argument
N = sys.argv[1]

# Check if N is an integer
if not N.isdigit():
    print("N must be a number")
    sys.exit(1)

N = int(N)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Create an empty NxN board
board = [[0] * N for _ in range(N)]

# Solve the N-Queens problem
solve_nqueens(board, 0)
