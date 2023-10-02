#!/usr/bin/python3
import sys

def solve_n_queens(N):
    def is_safe_to_place(pos, positions_on_chessboard):
        for i in range(len(positions_on_chessboard)):
            if positions_on_chessboard[i] == pos or \
                    positions_on_chessboard[i] - i == pos - len(positions_on_chessboard) or \
                    positions_on_chessboard[i] + i == pos + len(positions_on_chessboard):
                return False
        return True

    def place_queens_on_board(positions_on_chessboard, current_row, N):
        if current_row == N:
            solutions.append(positions_on_chessboard.copy())
            return
        for column in range(N):
            if is_safe_to_place(column, positions_on_chessboard):
                place_queens_on_board(positions_on_chessboard + [column], current_row + 1, N)

    solutions = []
    place_queens_on_board([], 0, N)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])
