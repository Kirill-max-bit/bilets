# Напишите алгоритм, который удаляет дубликаты из массива целых чисел. Изобразите блок-схему.


def remove_duplicates(arr):
    # Используем множество для удаления дубликатов
    unique_elements = set(arr)
    # Преобразуем множество обратно в список
    return list(unique_elements)

# Пример использования
arr = [1, 2, 2, 3, 4, 4, 5, 5, 5]
result = remove_duplicates(arr)
print("Массив без дубликатов:", result)
