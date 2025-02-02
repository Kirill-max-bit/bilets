#Создайте алгоритм для вычисления факториала заданного числа N. Изобразите блок-схему.


n = int(input("Введите целое число N: "))

if n < 0:
    print("Факториал отрицательного числа не определен")
else:
    factorial_result = 1
    for i in range(1, n + 1):
        factorial_result *= i
    print(f"Факториал {n}! = {factorial_result}")
