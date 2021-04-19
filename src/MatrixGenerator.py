import numpy as np
from Seidel import checkDiagonal


# actually this sucks a lot. Too many shit words like lambda or list. JS is better in one string programs))
def generateMatrix(n):
    matrix = list(map(lambda line: list(map(lambda el: round(el * 10), line)), list(np.random.rand(n, n + 1))))
    for i in range(n):
        matrix[i][i] = matrix[i][i] * 100
    return matrix


def generateMatrixWithDiagonal(n):
    matrix = generateMatrix(n)
    while checkDiagonal(matrix) != 1:
        matrix = generateMatrix(n)


# wow that's looks cooler than map variant
def generateMatrixCool(n):
    return [[round(el * 10) for el in line] for line in np.random.rand(n, n + 1)]
