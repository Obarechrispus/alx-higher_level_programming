#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        result_row = []

        for element in row:
            result_row.append(element ** 2)
        result.append(result_row)
    return result
