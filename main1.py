# Напишите программу, которая принимает целое число и определяет, является ли оно четным или нечетным. Изобразите блок-схему.

num = int(input("Введите целое число: "))
if num % 2 == 0:
    print(f"{num} — четное число")
else:
    print(f"{num} — нечетное число")
