# Напишите алгоритм, который ищет заданный элемент в массиве (линейный поиск). Изобразите блок-схему.


def linear_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Возвращаем индекс первого найденного элемента
    return -1  # Элемент не найден

# Пример использования
arr = [4, 2, 9, 7, 5, 1]
target = 7

result = linear_search(arr, target)
if result != -1:
    print(f"Элемент {target} найден на позиции {result}.")
else:
    print(f"Элемент {target} отсутствует в массиве.")
