import random as rand
import numpy as np

file = open('matrixInfo', 'w')

n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))
while n >= m:
    matrix = np.array([[rand.randint(0, 10) for j in range(m)] for i in range(n)])
    print("Входная матрица: ")
    print(matrix)
    print("Полученная матрица не является прямоугольной;\nПовторите ввод ниже")
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))
matrix = np.array([[rand.randint(0, 10) for j in range(m)] for i in range(n)])
print("Входная матрица: ")
print(matrix)
file.write(str(n) + " " + str(m))
file.write("\n" + str(matrix) + "\n")
l = int(input("Введите номер строки, в место которой вставиться новая строка: "))
while l > n:
    print('Количество строк в матрице: %d, введенное номер больше %d;\nПовторите ввод' % (n, n))
    l = int(input("Введите номер строки, в место которой вставиться новая строка: "))
strMat = np.array([rand.randint(0, 10) for i in range(m)])
print("Полученная строка: \n", strMat)
file.write("\n" + str(l))
matrix = np.insert(matrix, l, strMat, axis = 0)
print("Выходная матрица: \n", matrix, "\nКонец программы.")
file.write("\n" + str(strMat) + "\n")
file.write("\n" + str(matrix))
file.close()
