# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from math import factorial
from random import randint

# С функцией factorial


def fact(n):
    for arg in range(1, n+1):
        yield factorial(arg)


num = randint(1, 10)
print('Случайное число от 1 до 10:', num)
print('Список факториалов первых', num, ' натуральных чисел:')
for el in fact(num):
    print(el)

# С функцией "факториал", прописанной вручную


def fact_manual(number):
    answer = 1
    lst = list(range(1, number + 1))
    print('Факториал', lst[-1])
    for i in range(lst[-1]):
        answer *= lst[i]
    return answer


def fact2(n):
    for arg in range(1, n + 1):
        yield fact_manual(arg)


num = randint(1, 10)
print('Случайное число от 1 до 10:', num)
print('Список факториалов первых', num, ' натуральных чисел:')
for el in fact2(num):
    print(el)
