#Задание 1

import math
while True:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    print("Выберите операцию:")
    print("+. Сложение")
    print("-. Вычитание")
    print("*. Умножение")
    print(":. Деление")
    print("**. Возведение в степень")
    print("End. Выйти")

    choice = input("Введите операцию (+/-/*/:/End): ")


    if choice == 'End':
        print("Выход из программы.")
        break

    if choice in ('+', '-', '*', ':','**'):
        if choice == '+':
            result = num1 + num2
            operation = "сложения"
        elif choice == '-':
            result = num1 - num2
            operation = "вычитания"
        elif choice == '*':
            result = num1 * num2
            operation = "умножения"
        elif choice == ':':
            if num2 == 0:
                print("Ошибка: нельзя делить на ноль")
                continue
            else:
                result = num1 / num2
                operation = "деления"
        elif choice == '**':
            result = math.pow(num1, num2)
            operation = "возведения в степень"

        print(f"Результат {operation}: {result}")
    else:
        print("Ошибка: неверный выбор операции")