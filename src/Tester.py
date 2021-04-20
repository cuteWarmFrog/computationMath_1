import MatrixGenerator
from Seidel import Solve


def testOnRandomMatrices(n, accuracy):
    norm = 0
    neNorm = 0
    for i in range(n):
        print(str(i) + " test \n")
        matrix = MatrixGenerator.generateMatrixCool(2)
        answer, iterations = Solve(matrix, accuracy)
        if len(answer) > 0:
            norm += 1
            print('Итараций:', iterations)
            print('Ответ:', answer)
        else:
            neNorm += 1
            print("Достингуто пиковое число итераций. Итерации расходятся :(")

    print(norm)
    print(neNorm)


testOnRandomMatrices(1000, 0.001)
