#!/usr/bin/python3
"""
Class Divided all elements
function matrix_divided
parametres: matrix, div
Return: new_matrix
"""


def matrix_divided(matrix, div):
    """Returns all elements divided in the matrix"""
    mess_error1 = "matrix must be a matrix (list of lists) of integers/floats"
    mess_error2 = "Each row of the matrix must have the same size"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError(mess_error1)
    
    new_matrix=matrix
    row=1
    col=1
    a=0
    for row in range (len(new_matrix)):
        if type(row) not in [int, float]:
            raise TypeError(mess_error1)
        for col in range (len(new_matrix[row])):
            if type(col) not in [int, float]:
                raise TypeError(mess_error2)
            """new_matrix.append(round((new_matrix[row][col])/div,2))"""
            new_matrix[row][col] = round((new_matrix[row][col])/div,2)

    return new_matrix
    

