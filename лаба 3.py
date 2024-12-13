import random

a = []
b = 0

i = 0
while(i < 10):
    rand = random.randint(0, 100)
    b = b + rand
    a.append(rand)
    i = i + 1

print("Сгенерированные числа:", a)

# Сортировка списка
sorted_a = sorted(a)
print("Отсортированные числа:", sorted_a)

# Нахождение максимального значения
max_value = max(a)
print("Максимальное значение:", max_value)

# Нахождение минимального значения
min_value = min(a)
print("Минимальное значение:", min_value)

# Вывод суммы значений
print("Сумма значений:", b)