from random import randint
_author_ = "Saranchin K.A."


# https://ivtipm.github.io/Programming/Glava07/index07.htm#z178
print(" Даны натуральные числа n, a 1...an. Определить количество членов ak последовательности a1,...,an:\n "
      "е) имеющих четные порядковые номера и являющихся нечетными числами.")

s = 1
s1 = 0
print("Введите количество элементов: ")
n = int(input())
arr = []
print("Элементы массива: ")
for i in range(n):
    # arr.append(randint(-20, 20))
    arr = (randint(-20, 20))
    # print(arr[::2])
    print(f"[{i}]", arr)
    if i % 2 != 0 and arr % 2 == 0:
        print("Подходит под условие:", arr)
        s1 += 1

print("Количество элементов, подходящих под условие =", s1)

