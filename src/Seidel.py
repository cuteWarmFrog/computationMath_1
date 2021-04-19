import numpy as np


def Solve(matrix, accuracy):
    if checkDiagonal(matrix):
        return Seidel(matrix, accuracy)
    else:
        return [], 0


def checkDiagonal(matrix):
    diagonal = 1
    for i in range(len(matrix)):
        s1 = sum(abs(matrix[i][j]) for j in range(i))
        s2 = sum(abs(matrix[i][j]) for j in range(i + 1, len(matrix)))
        if abs(matrix[i][i]) < s1 + s2:
            diagonal = 0
    return diagonal == 1


def Seidel(matrix, accuracy):
    n = len(matrix)
    x = [0.] * n

    converge = False
    iterations = 0
    while not converge:
        if iterations > 1000:
            return [], iterations

        iterations += 1
        xNew = np.copy(x)
        for i in range(n):
            s1 = sum(matrix[i][j] * xNew[j] for j in range(i))
            s2 = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
            xNew[i] = (matrix[i][n] - s1 - s2) / matrix[i][i]
        for i in range(n):
            converge = abs(xNew[i] - x[i]) <= accuracy
        x = xNew

    return x, iterations
