import itertools
import Seidel
import sys


def findDiagonal(matrix):
    if len(matrix) > 10:
        print("Перестановок для 11 элементов - 39916800. Мы здесь просидим до утра.")
        sys.exit()
    for matrix in itertools.permutations(matrix, len(matrix)):
        if Seidel.checkDiagonal(list(matrix)):
            return list(matrix)

    return False


