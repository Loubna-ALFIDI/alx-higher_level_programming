#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = [list(row) for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            square[i][j] = matrix[i][j] * matrix[i][j]
    return square
