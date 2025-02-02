# Реализуйте алгоритм сортировки массива (например, пузырьковая сортировка) и изобразите его в виде блок-схемы.


def bubble_sort(arr):
    for _ in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
print("Отсортированный массив:", bubble_sort(arr.copy()))
