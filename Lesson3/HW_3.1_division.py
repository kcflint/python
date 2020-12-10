# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
# деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
# ноль.


dividend = int(input('Введите делимое: '))
divisor = int(input('Введите делитель: '))


def division(arg1, arg2):
    try:
        print(f'Частное: ', arg1 / arg2)
    except ZeroDivisionError:
        print('Деление на ноль')


division(dividend, divisor)
