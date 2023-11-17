_author_ = "Saranchin K.A."

print("Вычислить: Сумма(n,k=1) k(k+1)...k**2")

print("Введите n")
n = int(input())
k = 1
s = 0
for k in range(n):
    c = 1
    for j in range(k):
        c = c * (k + j)
    s = s + c
    print(s)
print("Результат =", s)
