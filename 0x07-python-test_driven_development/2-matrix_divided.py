#!/usr/bin/python3
"""
    function that divides all elements of a matrix.
    all elements must be integer or float, and divisor
    must not be zero
"""


def matrix_divided(matrix, div):
    """function prototype"""

    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]
    
    return new_matrix
