# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369.

number1 = int(input('Введите цифру от 1 до 9: '))
number2 = str(number1)*2
number3 = str(number1)*3
total = number1 + int(number2) + int(number3)

print(f'{number1}+{number2}+{number3}={total}')
