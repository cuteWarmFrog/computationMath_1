import numpy as np
import Reader


def greet():
    print('Приветствую тебя, странник.\nЧувствуй себя как дома, но не забывай, что ты в гостях.\n')


greet()
answer = input('Напиши (1), если хочешь ввести матрицы вручную или (2), если из файла.\n')

matrix = Reader.readMatrix(answer)

if matrix is not None:
    print('Ваша матрица:')
    for line in matrix:
        print(line)
else:
    print('Вы запостили кринж, весь город должен умереть!')