import numpy as np


def generateMatrix(n):
    matrix = np.random.rand(n, n + 1)
    for i in range(n):
        for j in range(n + 1):
            matrix[i][j] = round(matrix[i][j] * 10)
    return matrix
