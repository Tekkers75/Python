# https://ivtipm.github.io/Programming/Glava20/index20.htm#z676
__author__ = "Saranchin K.A."

# Пример исходной матрицы
matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24, 25, 26, 27],
    [28, 29, 30, 31, 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42, 43, 44, 45],
    [46, 47, 48, 49, 50, 51, 52, 53, 54]
]

n = len(matrix)
m = len(matrix[0])

# Создаем новую матрицу, в которую будем записывать перестановку строк
new_matrix = [[0 for _ in range(m)] for _ in range(n)]

# Выполняем перестановку строк
for i in range(n):
    new_matrix[i] = matrix[n - 1 - i]

# Выводим результат
for row in new_matrix:
    print(row)
