# Напишите программу, которая вычисляет сумму всех целых чисел от 1 до N. Изобразите блок-схему.


n = int(input("Введите целое число N: "))

# Метод 1: Использование цикла
total_loop = 0
if n >= 1:
    for i in range(1, n + 1):
        total_loop += i

# Метод 2: Формула Гаусса
total_formula = n * (n + 1) // 2 if n >= 1 else 0

print(f"[Цикл] Сумма от 1 до {n} = {total_loop}")
print(f"[Формула] Сумма от 1 до {n} = {total_formula}")
