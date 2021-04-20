import numpy as np
from Seidel import checkDiagonal
from DiagonalFinder import findDiagonal


# actually this sucks a lot. Too many shit words like lambda or list. JS is better in one string programs))
def generateMatrix(n):
    matrix = list(map(lambda line: list(map(lambda el: round(el * 10) + 1, line)), list(np.random.rand(n, n + 1))))
    for i in range(n):
        matrix[i][i] = matrix[i][i] * 10
    return matrix


def generateMatrixWithDiagonal(n):
    matrix = generateMatrix(n)
    while not findDiagonal(matrix):
        matrix = generateMatrix(n)
    return matrix


# wow that's looks cooler than map variant
def generateMatrixCool(n):
    return [[round(el * 10) + 1 for el in line] for line in np.random.rand(n, n + 1)]


generatedMatrix = generateMatrixWithDiagonal(8)
for line in generatedMatrix:
    print(" ".join([str(el) for el in line]))
