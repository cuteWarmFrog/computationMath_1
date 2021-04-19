from MatrixGenerator import generateMatrix
from Seidel import Seidel


def testOnRandomMatrices(n, accuracy):
    for i in range(n):
        print(str(i) + " test \n")
        matrix = generateMatrix(n)
        answer, iterations = Seidel(matrix, accuracy)
        if answer:
            print('Итараций:', iterations)
            print('Ответ:', answer)
        else:
            print("Достингуто пиковое число итераций. Итерации расходятся :(")


testOnRandomMatrices(8, 0.001)
