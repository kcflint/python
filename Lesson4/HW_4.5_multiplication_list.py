# Реализовать формирование списка, используя функцию range() и возможности генератора. В список
# должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления
# произведения всех элементов списка.
# Подсказка: использовать функцию reduce() .
from functools import reduce

new_list = [el for el in range(100, 1001) if el % 2 == 0]


def mult_func(prev_el, el):
    return prev_el * el


print('Список всех четных чисел от 100 до 1000 включая границы')
print(new_list)
print('Произведение всех четных чисел от 100 до 1000 включая границы')
print(reduce(mult_func, new_list))
