#!/usr/bin/python3
"""
Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix
You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    """
    a function with matrix and div as parameter, with the first conditional statement testing if the content of the matrix is a list

    """
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


