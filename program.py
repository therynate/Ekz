def convert_case():
    # Запрос строки у пользователя
    user_input = input("Введите строку: ")

    # Преобразование строки в нижний регистр
    lower_case = user_input.lower()
    # Преобразование строки в верхний регистр
    upper_case = user_input.upper()

    # Вывод результатов
    print(f"Строка в нижнем регистре: {lower_case}")
    print(f"Строка в верхнем регистре: {upper_case}")

# Запуск функции
convert_case()
