#Задание 1
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

print("Выберите операцию:")
print("+. Сложение")
print("-. Вычитание")
print("*. Умножение")
print(":. Деление")

choice = input("Введите операцию (+/-/*/:): ")

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
        result = num1 / num2
        operation = "деления"

if result is not None:
    print(f"Результат {operation}: {result}")
