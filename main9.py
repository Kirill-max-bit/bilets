# Реализуйте алгоритм сортировки массива (например, пузырьковая сортировка) и изобразите его в виде блок-схемы.


# Определение функции пузырьковой сортировки
def bubble_sort(arr):
    # Внешний цикл: повторяем столько раз, сколько элементов в массиве
    for _ in range(len(arr)):
        # Внутренний цикл: проходим по всем элементам, кроме последнего
        for j in range(len(arr)-1):
            # Сравниваем текущий элемент со следующим
            if arr[j] > arr[j+1]:
                # Меняем элементы местами, если текущий больше следующего
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # Возвращаем отсортированный массив
    return arr

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
# Вызываем функцию с копией массива, чтобы оригинал остался неизменным
print("Отсортированный массив:", bubble_sort(arr.copy())) 
