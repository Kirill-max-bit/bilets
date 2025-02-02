def calculate_average(numbers):
    if not numbers:  # Проверка на пустой массив
        return 0
    return sum(numbers) / len(numbers)  # Сумма / количество

# Пример использования
numbers = [2, 3, 5, 7, 11]
average = calculate_average(numbers)
print(f"Среднее арифметическое: {average}")
