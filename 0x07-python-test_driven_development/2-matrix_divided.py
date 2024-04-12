#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list")
    if not all (isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of list")
    if not all (isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError("matrix must be a matrix of integersa and floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError ("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]

    return new_matrix


