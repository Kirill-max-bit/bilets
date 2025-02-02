def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Множество гласных
    count = 0
    for char in text.lower():  # Игнорируем регистр
        if char in vowels:
            count += 1
    return count

# Пример использования
text = input("Введите текст: ")
print(f"Количество гласных: {count_vowels(text)}")
