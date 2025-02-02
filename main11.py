# Создайте программу, которая конвертирует температуру из Цельсия в Фаренгейт и наоборот. Изобразите блок-схему.


# Конвертация Цельсий ↔ Фаренгейт (базовая версия)
choice = input("Конвертировать:\n1. C → F\n2. F → C\nВыберите 1/2: ")
temp = float(input("Температура: "))  # Ввод числа

if choice == '1':
    print(f"Результат: {(temp * 9/5) + 32:.1f}°F")  # Формула C→F
elif choice == '2':
    print(f"Результат: {(temp - 32) * 5/9:.1f}°C")  # Формула F→C
else:
    print("Ошибка: выберите 1 или 2")