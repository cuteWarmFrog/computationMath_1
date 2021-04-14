import numpy as np


def Seidel(matrix, accuracy):
    n = len(matrix)
    b = [matrix[i][n] for i in range(n)]
    x = np.zeros(n)
    converge = False

    iterations = 0
    while not converge:
        iterations += 1
        xNew = np.copy(x)
        for i in range(n):
            s1 = sum(matrix[i][j] * xNew[j] for j in range(i))
            s2 = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
            xNew[i] = (b[i] - s1 - s2) / matrix[i][i]

        converge = np.sqrt(sum((xNew[i] - x[i]) ** 2 for i in range(n))) <= accuracy
        x = xNew

    return x, iterations
