# Напишите алгоритм, который проверяет, является ли строка палиндромом. Изобразите блок-схему.


# Определяем функцию для проверки, является ли строка палиндромом
def is_palindrome(s):
    # Удаляем пробелы из строки и приводим все символы к нижнему регистру
    # Пример: "А роза" → "ароза"
    s = s.replace(" ", "").lower()  
    
    # Сравниваем исходную строку с её обратной версией (срез [::-1] разворачивает строку)
    # Возвращаем True, если строки равны (это палиндром), иначе False
    return s == s[::-1]  

# Пример использования
input_str = input("Введите строку: ")  # Получаем строку от пользователя

if is_palindrome(input_str):  # Вызываем функцию проверки
    print("Это палиндром!")   # Если вернулось True
else:
    print("Это не палиндром.")  # Если вернулось False
