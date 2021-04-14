import numpy as np
import Reader
import Seidel
import sys


def greet():
    print('Приветствую тебя, странник.\nЧувствуй себя как дома, но не забывай, что ты в гостях.\n')


greet()
consoleOrFile = input('Напиши (1), если хочешь ввести матрицы вручную или (2), если из файла.\n')

matrix = Reader.readMatrix(consoleOrFile)

if matrix is None:
    sys.exit('Вы ввели кринж. Теперь весь город должен умереть.')

det = np.linalg.det([line[:len(line) - 1] for line in matrix])

if round(det, 3) == 0:
    print("Определитель - 0, жизнь не имеет смысла")
    sys.exit()

accuracy = float(input('Введите желаемую точность:\n'))

answer, iterations = Seidel.Seidel(matrix, accuracy)

print('Итараций:', iterations)
print('Ответ:', answer)
