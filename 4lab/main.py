_author_ = "Saranchin K.A."

print("Вычислить произведение ((i + 1)/(i + 2)), 100 раз, начиная с 2")
# i = 2
p = 1
for i in range(2, 100):
    p = p * ((i + 1)/(i + 2))
   # print(f"{p:.4f}")
print(f"Результат вычисления = {p:.4f}")
