# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = 0
while number <= 0:
    number = int(input('Введите целое положительное число: '))

max_number = 0
number_n = number

for i in range(len(str(number))):
    digit = number_n // 10**(len(str(number))-i)
    if digit > max_number:
        max_number = digit
    number_n = number_n - (digit * 10**(len(str(number))-i))
print(f'Самая большая цифра в числе {number} - {max_number}')
