# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
# возвращает сумму наибольших двух аргументов.

number1 = int(input('Введите первое число '))
number2 = int(input('Введите второе число '))
number3 = int(input('Введите третье число '))

# Первый способ


def my_func1(arg1, arg2, arg3):
    if arg1 > arg2:
        minimum = arg2
    else:
        minimum = arg1
    if minimum > arg3:
        minimum = arg3
    return arg1 + arg2 + arg3 - minimum


print('Первый способ', my_func1(number1, number2, number3))

# Второй способ


def my_func2(arg1, arg2, arg3):
    user_list = []
    user_list.append(arg1)
    user_list.append(arg2)
    user_list.append(arg3)
    user_list = sorted(user_list)
    return user_list[-1] + user_list[-2]


print('Второй способ', my_func2(number1, number2, number3))

# Третий способ


def my_func3(arg1, arg2, arg3):
    return (arg1 + arg2 + arg3) - min(arg1, arg2, arg3)


print('Третий способ', my_func3(number1, number2, number3))
