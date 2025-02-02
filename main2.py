#напишите алгоритм, который принимает три числа и находит максимальное из них. Изобразите блок-схему.


a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a >= b and a >= c:
    maximum = a
elif b >= c:
    maximum = b
else:
    maximum = c

print(f"Максимальное число: {maximum}")
