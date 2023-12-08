from matrix import swap_rows

# Вызов функции с указанием всех параметров
matrix = [[5.6, 6.7, 8.9],
          [5.8, 9.9, 2.0],
          [7.0, 8.4, 9.0]]
result = swap_rows(matrix)
# print(result)
for row in result:
    print(row)

print()

# Вызов функции с указанием только конкретных параметров
matrix = [[65.1, 23.8], [55.8, 45.5]]
result = swap_rows(matrix)
# print(result)
for row in result:
    print(row)
print()


# Вызов функции без параметров
#result = matrix_func_transpose()
#print(result)

# Лямбда-функция для вычисления математического выражения
math_expression = lambda x, y, z: x + y + z

# Пример использования
result = math_expression(55.8, 4.2, 77)
print(result)



