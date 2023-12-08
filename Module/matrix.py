from typing import List
# Функция преобразования матрицы
def swap_rows(matrix: List[List[float]]) -> List[List[float]]:
    # Функция принимает матрицу из списка из списков чисел типа float.
    # Возвращает List[List[float]
    # Проверка входных данных
    assert isinstance(matrix, list), "Аргумент 'matrix' должен быть списком."
    assert all(isinstance(row, list) for row in matrix), "Матрица должна быть представлена списком списков."
    assert all(all(isinstance(element, float) for element in row) for row in matrix), "Элементы матрицы должны быть числами с плавающей точкой."
    n = len(matrix)
    m = len(matrix[0])


    # Создаем новую матрицу, в которую будем записывать перестановку строк
    new_matrix = [[0 for _ in range(m)] for _ in range(n)]

    # Выполняем перестановку строк
    for i in range(n):
        new_matrix[i] = matrix[n - 1 - i]

    return new_matrix