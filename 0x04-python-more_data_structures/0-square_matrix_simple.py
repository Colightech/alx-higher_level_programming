#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = matrix.copy()
    matrix_len = len(matrix)
    for z in range(matrix_len):
        matrix_copy[z] = list(map(lambda x: x**2, matrix[z]))
    return (matrix_copy)
