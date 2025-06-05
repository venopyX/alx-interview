#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotates a 2D square matrix 90 degrees clockwise in place.

    Parameters:
        matrix (list of list): The matrix to rotate.

    Returns:
        None: The matrix is rotated in place.
    """
    n = len(matrix)
    for i in range(n // 2):
        y = n - i - 1
        for j in range(i, y):
            x = n - 1 - j
            tmp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[y][x]
            matrix[y][x] = matrix[j][y]
            matrix[j][y] = tmp
