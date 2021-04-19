import MatrixGenerator
from Seidel import Solve


def testOnRandomMatrices(n, accuracy):
    norm = 0
    nenorm = 0
    for i in range(n):
        print(str(i) + " test \n")
        matrix = MatrixGenerator.generateMatrixMap(4)
        answer, iterations = Solve(matrix, accuracy)
        if len(answer) > 0:
            norm += 1
            # print('Итараций:', iterations)
            # print('Ответ:', answer)
        else:
            nenorm += 1
            # print("Достингуто пиковое число итераций. Итерации расходятся :(")

    print(norm)
    print(nenorm)


testOnRandomMatrices(100000, 0.01)
