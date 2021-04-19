import numpy as np
from Seidel import checkDiagonal

# actually this sucks a lot. Too many shit words like lambda or list. JS is better in one string programs))
def generateMatrixMap(n):
    matrix = list(map(lambda line: list(map(lambda el: round(el * 10), line)), list(np.random.rand(n, n + 1))))
    for i in range(n):
        matrix[i][i] = matrix[i][i] * 100
    return matrix


def generateMatrixWithDiagonal(n):
    matrix = generateMatrixMap(n)
    while checkDiagonal(matrix) != 1:
        matrix = generateMatrixMap(n)


# this looks better but does not work lol todo make this shit work
def generateMatrixCool(n):
    return list([round(el * 10) for el in [line for line in [np.random.rand(n, n + 1)]]])
