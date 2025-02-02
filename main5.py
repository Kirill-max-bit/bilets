# Напишите программу, которая проверяет, является ли заданное число простым. Изобразите блок-схему.


import math

n = int(input("Введите целое число: "))

if n <= 1:
    is_prime = False
elif n == 2:
    is_prime = True
elif n % 2 == 0:
    is_prime = False
else:
    is_prime = True
    max_divisor = math.isqrt(n) + 1  # Вычисляем корень и округляем вверх
    for i in range(3, max_divisor, 2):  # Проверяем только нечетные делители
        if n % i == 0:
            is_prime = False
            break

print(f"Число {n} {'простое' if is_prime else 'не является простым'}")
