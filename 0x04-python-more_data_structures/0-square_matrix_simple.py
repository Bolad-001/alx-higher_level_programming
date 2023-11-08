#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mat = []

    for mat_arr in matrix:
        y = [x ** 2 for x in mat_arr]
        new_mat.append(y)
    return new_mat
    '''return [list(map(lambda a: a ** 2, mat_arr)) for mat_arr in matrix]'''
