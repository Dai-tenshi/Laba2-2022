"""
Вычислить сумму знакопеременного ряда |х^(4n-1)|/(2n)!,
где х-матрица ранга к (к и матрица задаются случайным образом),
n - номер слагаемого. Сумма считается вычисленной, если точность вычислений будет не меньше t знаков после запятой.
 У алгоритма д.б. линейная сложность. Операция умножения –поэлементная
"""



import numpy as np
from numpy import linalg

matrix = int(input('Введите размерность квадратной матрицы больше 1 и меньше 15:'))
while (matrix < 1) or (matrix > 15):
    matrix = int(input("Введите указанные числа"))
razmer = np.random.randint(5, size=(matrix, matrix))
print("Матрица:\n", razmer)

znak = int(input('Введите количество знаков после запятой:'))
znak = 0.1 ** znak
n = 1
factorial = 1
summa = 0
fg = 0
out = 1
while abs(out) > znak:
    fg += summa
    summa += (np.linalg.det(linalg.matrix_power(razmer, 4 * n - 1))) / factorial
    n += 1
    factorial = factorial * (4*n - 1) * 2*n
    out = abs(fg-summa)
    fg = 0
    print(n-1, ':', summa, ' ', out)
print('Сумма знакопеременного ряда:', summa)