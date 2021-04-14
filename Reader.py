def readMatrix(consoleOrFile):
    if consoleOrFile == '1':
        return readFromConsole()
    elif consoleOrFile == '2':
        return readFromFile()
    else:
        print('No i am going to die.')
        return None


def readFromConsole():
    matrix = []
    n = int(input('Какая размерность у матрицы?'))
    for i in range(n):
        matrix.append(map(lambda x: float(x), input().split(' ')))
    return matrix


def readFromFile():
    matrix = []
    f = open('test.txt', 'r')
    for line in f:
        matrix.append(list(map(lambda x: float(x), line.split(' '))))
    return matrix
