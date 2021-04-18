import numpy as np
import math


# todo something not working here. need to fix double overflowing in sums;

def Seidel(matrix, accuracy):
    n = len(matrix)
    x = np.zeros(n)

    converge = False
    iterations = 0
    while not converge:
        iterations += 1
        xNew = np.copy(x)
        for i in range(n):
            s1 = sum(matrix[i][j] * xNew[j] for j in range(i))
            s2 = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
            xNew[i] = (matrix[i][n] - s1 - s2) / matrix[i][i]
            print(iterations)
        for i in range(n):
            converge = abs(xNew[i] - x[i]) <= accuracy
        x = xNew

    return x, iterations
