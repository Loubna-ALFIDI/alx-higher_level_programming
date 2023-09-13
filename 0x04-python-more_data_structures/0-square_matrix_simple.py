#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = [list(row) for row in matrix]
    for i in range(len(square)):
        for j in range(len(square)):
            square[i][j] = square[i][j] ** 2
    return square
