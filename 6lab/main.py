from math import *
from random import *
_author_ = "Saranchin K.A."


# https://ivtipm.github.io/Programming/Glava06/index06.htm#z136
# print("Вычислить: ")

s = 1
s1 = 0
print("Введите количество элементов: ")
n = int(input())
arr = []
print("Элементы массива: ")
for i in range(n):
    arr = (randint(-20, 20))
    if arr == 0:
        arr = arr + 1
    print(arr, end=" ")
    # s = (s + l)
    # s1 = 2 * (pow(s, 2))
    s = abs(s * arr)
    s1 = sqrt(s)

print()
print("Произведение элементов массива =", s)
print("Итоговый результат =", s1)

