# Создайте программу, которая генерирует N первых чисел последовательности Фибоначчи. Изобразите блок-схему.


def generate_fibonacci(n):
    # Первые два числа последовательности Фибоначчи
    fibonacci_sequence = [0, 1]
    
    # Генерация последующих чисел
    for i in range(2, n):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    # Возвращаем первые N чисел
    return fibonacci_sequence[:n]

# Ввод числа N от пользователя
n = int(input("Введите количество чисел последовательности Фибоначчи: "))

# Генерация и вывод последовательности
if n <= 0:
    print("Пожалуйста, введите положительное число.")
else:
    result = generate_fibonacci(n)
    print(f"Первые {n} чисел последовательности Фибоначчи: {result}")
